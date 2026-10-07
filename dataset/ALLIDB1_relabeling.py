import argparse
import hashlib
import json
import math
import shutil
import sys
from pathlib import Path

try:
    from PIL import Image, ImageFile
except ImportError:
    raise SystemExit('Pillow is required. Install it with: python3 -m pip install Pillow')

ImageFile.LOAD_TRUNCATED_IMAGES = False
SUPPORTED_IMAGES = {'.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp'}


def read_centroids(path, width, height, one_based=False):
    """Read (x, y) in pixels, preserving supplied coordinates by default."""
    points = []
    seen = set()
    for line_number, line in enumerate(path.read_text(encoding='utf-8-sig').splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 2:
            raise ValueError(f'{path.name}:{line_number}: expected exactly two coordinates')
        try:
            x, y = map(float, fields)
        except ValueError:
            raise ValueError(f'{path.name}:{line_number}: non-numeric coordinate') from None
        if not (math.isfinite(x) and math.isfinite(y)):
            raise ValueError(f'{path.name}:{line_number}: coordinate must be finite')
        if one_based:
            x, y = x - 1, y - 1
        if not (0 <= x < width and 0 <= y < height):
            raise ValueError(f'{path.name}:{line_number}: ({x}, {y}) outside {width}x{height}')
        if (x, y) in seen:
            raise ValueError(f'{path.name}:{line_number}: duplicate centroid ({x}, {y})')
        seen.add((x, y))
        points.append((x, y))
    return points


def make_annotation(image_name, width, height, points, point_label):
    """Native XLABEL/LabelMe-style point shapes; one instance per centroid."""
    return {
        'version': '3.0.0',
        'flags': {},
        'shapes': [
            {
                'label': point_label,
                'score': None,
                'points': [[x, y]],
                'group_id': index,
                'description': 'Imported blast centroid from ALL-IDB1 .xyc; bounding box pending.',
                'difficult': False,
                'shape_type': 'point',
                'flags': {},
                'attributes': {},
                'kie_linking': [],
            }
            for index, (x, y) in enumerate(points, 1)
        ],
        'imagePath': image_name,
        'imageData': None,
        'imageHeight': height,
        'imageWidth': width,
        'description': 'Centroid reference points for manual YOLO detection relabeling.',
        'checked': False,
    }


def scan_dataset(dataset, point_label, one_based=False):
    image_dir = dataset / 'im'
    coordinate_dir = dataset / 'xyc'
    if not image_dir.is_dir() or not coordinate_dir.is_dir():
        raise ValueError('The dataset must contain im/ and xyc/ directories')
    images = sorted(p for p in image_dir.iterdir() if p.is_file() and p.suffix.lower() in SUPPORTED_IMAGES)
    if not images:
        raise ValueError(f'No supported images found in {image_dir}')
    if len({p.stem for p in images}) != len(images):
        raise ValueError('Multiple image files share a stem; output JSON names would collide')
    extra_coordinates = sorted(p.name for p in coordinate_dir.glob('*.xyc') if p.stem not in {im.stem for im in images})
    if extra_coordinates:
        raise ValueError(f'Unpaired .xyc files: {extra_coordinates}')

    unique = []
    duplicates = []
    seen_hashes = {}
    for image_path in images:
        coordinate_path = coordinate_dir / (image_path.stem + '.xyc')
        if not coordinate_path.is_file():
            raise ValueError(f'Missing annotation: {coordinate_path}')
        raw = image_path.read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        with Image.open(image_path) as image:
            width, height = image.size
            orientation = image.getexif().get(274, 1)
            image.verify()
        with Image.open(image_path) as image:
            image.load()
        if min(width, height) < 10:
            raise ValueError(f'{image_path.name}: image dimensions must be at least 10 pixels')
        if orientation != 1:
            raise ValueError(f'{image_path.name}: EXIF orientation {orientation} requires explicit coordinate handling')
        points = read_centroids(coordinate_path, width, height, one_based)
        label_token = image_path.stem.rsplit('_', 1)[-1]
        if label_token not in {'0', '1'}:
            raise ValueError(f'{image_path.name}: expected ALL-IDB1 _0 or _1 filename label')
        image_label = int(label_token)
        if bool(points) != bool(image_label):
            raise ValueError(f'{image_path.name}: filename label disagrees with centroid presence')

        record = {
            'path': image_path,
            'coordinate_path': coordinate_path,
            'sha256': digest,
            'width': width,
            'height': height,
            'points': points,
            'image_label': image_label,
        }
        if digest in seen_hashes:
            kept = seen_hashes[digest]
            if image_label != kept['image_label'] or sorted(points) != sorted(kept['points']):
                raise ValueError(f'Duplicate image files have conflicting labels: {kept["path"].name}, {image_path.name}')
            duplicates.append({'skipped': image_path.name, 'kept': kept['path'].name, 'sha256': digest})
            continue
        record['annotation'] = make_annotation(image_path.name, width, height, points, point_label)
        seen_hashes[digest] = record
        unique.append(record)
    return images, unique, duplicates


def write_json(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2, allow_nan=False) + '\n', encoding='utf-8')


def export_workspace(output, dataset, unique, manifest, point_label):
    if output == dataset or dataset in output.parents:
        raise ValueError('Output must be outside the source dataset directory')
    if output.is_symlink():
        raise ValueError('Output must not be a symbolic link')
    if output.exists() and (not output.is_dir() or any(output.iterdir())):
        raise ValueError('Output must be new or empty; existing relabeling work will not be overwritten')
    output.mkdir(parents=True, exist_ok=True)
    destination = output / 'images'
    destination.mkdir()
    for record in unique:
        image_path = record['path']
        copied_image = destination / image_path.name
        shutil.copy2(image_path, copied_image)
        if hashlib.sha256(copied_image.read_bytes()).hexdigest() != record['sha256']:
            raise ValueError(f'Copy verification failed: {image_path.name}')
        write_json(destination / (image_path.stem + '.json'), record['annotation'])
    write_json(output / 'conversion_manifest.json', manifest)
    (output / 'classes.txt').write_text('blast\n', encoding='utf-8')
    (output / 'README.md').write_text(
        '# ALL-IDB1 point annotation workspace\n\n'
        'Open the `images/` directory in X-AnyLabeling. Images and their native JSON labels are colocated.\n\n'
        f'Each `{point_label}` point is a blast centroid in pixel coordinates. Each cell has a separate `group_id`. '
        'Draw a rectangle labeled `blast` around the corresponding visible cell and give it the same `group_id`. '
        'Use four rectangle corner points if editing the JSON manually.\n\n'
        'Point-only labels are reference annotations, not a YOLO pose training dataset. '
        'A valid YOLO pose instance also requires a bounding box. '
        'For the planned detection task, export completed rectangles as YOLO detection annotations. '
        'Keep the point references in the master JSONs; the detection export must contain rectangle labels only.\n\n'
        'Negative images have empty `shapes` and must be retained when exporting the detection dataset. '
        'Validate the final rectangles visually and compare their counts with the imported centroid counts.\n\n'
        'All source images, including images with arrows, were kept unchanged except that exact duplicate files '
        'were excluded from this copy. The source dataset was not modified. '
        'See `conversion_manifest.json` for skipped filenames and counts.\n',
        encoding='utf-8',
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dataset', required=True, type=Path, help='ALL-IDB1 source directory containing im/ and xyc/')
    parser.add_argument('--output', required=True, type=Path, help='New or empty workspace directory, outside the source dataset')
    parser.add_argument('--point-label', default='blast_center', help='Keypoint label (default: blast_center)')
    parser.add_argument('--one-based-input', action='store_true', help='Subtract 1 from x and y; use ONLY if input origin is documented as one-based')
    parser.add_argument('--dry-run', action='store_true', help='Validate and report counts without writing files')
    args = parser.parse_args(argv)
    if not args.point_label.strip():
        parser.error('--point-label must not be blank')
    dataset = args.dataset.expanduser().resolve()
    output = args.output.expanduser().absolute()
    if output.is_symlink():
        parser.error('--output must not be a symbolic link')
    output = output.resolve()
    if output == dataset or dataset in output.parents:
        parser.error('--output must be outside the source dataset directory')
    try:
        images, unique, duplicates = scan_dataset(dataset, args.point_label, args.one_based_input)
        manifest = {
            'source_dataset': str(dataset),
            'output_workspace': str(output),
            'annotation_format': 'X-AnyLabeling native JSON point shapes',
            'point_label': args.point_label,
            'coordinates': 'one-based input shifted to zero-based' if args.one_based_input else 'pixel coordinates preserved as supplied',
            'source_image_count': len(images),
            'output_image_count': len(unique),
            'output_json_count': len(unique),
            'positive_image_count': sum(record['image_label'] == 1 for record in unique),
            'negative_image_count': sum(record['image_label'] == 0 for record in unique),
            'point_count': sum(len(record['points']) for record in unique),
            'rectangles_created': 0,
            'arrow_policy': 'All source images retained without pixel changes; no arrow removal filter applied.',
            'source_modified': False,
            'duplicates_skipped': duplicates,
            'images': [
                {'filename': record['path'].name, 'xyc_filename': record['coordinate_path'].name,
                 'sha256': record['sha256'], 'width': record['width'], 'height': record['height'],
                 'image_label': record['image_label'], 'point_count': len(record['points'])}
                for record in unique
            ],
        }
        if not args.dry_run:
            export_workspace(output, dataset, unique, manifest, args.point_label)
        summary = {key: value for key, value in manifest.items() if key != 'images'}
        summary['dry_run'] = args.dry_run
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    except (ValueError, OSError) as error:
        parser.exit(1, f'Error: {error}\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
