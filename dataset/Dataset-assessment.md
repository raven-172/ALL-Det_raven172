# ALL-IDB1 Assessment for YOLO

Inspection date: 7 October 2026. Source folder: `/Users/le/Desktop/ALLDet/dataset/ALL_IDB1`.

**Conclusion: the image files are readable and use a suitable format, but the current dataset is not yet ready for training YOLO for cell detection.** The main issues are missing bounding boxes, 15 images with arrows embedded in the source images, and one pair of exact duplicates.

## Results of the Full Dataset Inspection

| Item | Result |
|---|---|
| Images inspected | 108 |
| Full image decoding | 108/108; no corrupted or truncated images found |
| Format and color mode | 108 JPEG images, RGB |
| JPEG end markers | Valid in all 108 images |
| EXIF orientation | No images require rotation based on EXIF metadata |
| Dimensions | 33 images at 1712 × 1368; 74 images at 2592 × 1944; 1 image at 1226 × 652 |
| Unique images | 107 |
| Corresponding `.xyc` annotations | 108/108; no missing image–annotation pairs |
| `_1` group | 49 images containing at least one blast cell |
| `_0` group | 59 images containing no blast cells |
| Annotated blast centers | 510 points across 49 nonempty `.xyc` files |
| Coordinate checks | Every line contains 2 integers within the image boundaries; no duplicate points within any file |
| YOLO detection annotations | No bounding boxes or YOLO `.txt` annotations available |
| Train/val/test splits and dataset configuration | Not present in the inspected folder |

Differences in image dimensions are not format errors. In particular, `Im037_0.jpg` is 1226 × 652 and has a different aspect ratio from most of the dataset, but it still decodes normally.

## Issues That Need to Be Addressed

### 1. The Current Annotations Provide Centers Only, Not Bounding Boxes

For example, `Im001_1.xyc` contains pixel coordinate pairs such as `886 726`. According to the [official ALL-IDB description](https://scotti.di.unimi.it/all/index.php), these are the centers of blast cells. The `_0/_1` suffix in each image filename is a label for the **whole image**, not a label for every cell in that image.

YOLO-Detect requires one line per object in the form `class x_center y_center width height`, with coordinates normalized by the image width and height. The existing center points do not specify cell width and height, so they cannot be converted into valid bounding boxes simply by changing the file extension. See the [Ultralytics detection annotation format](https://docs.ultralytics.com/datasets/detect).

- For a **single-class `blast` detection task**: bounding boxes must be drawn and checked for the 510 marked cells; images without blast cells can serve as negative samples with empty annotations.
- For a **two-class `blast` and `normal` detection task**: normal cells also need annotations; the current dataset does not contain these labels.
- Placing a fixed-size box around each center produces approximate annotations, not verified bounding boxes.

### 2. Arrows Are Embedded in the Source Images: 15/49 Positive Images

A color scan of all 108 images, followed by visual inspection, confirmed that **15 images contain a yellow arrow with a pink outline**. All belong to the `_1` group; none appear in the `_0` group. These arrows are already present in the source JPEGs and were not added as an illustration layer during the inspection.

![Arrows in the source JPEGs](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_source_arrows.jpg)

Complete list: `Im002_1.jpg`, `Im007_1.jpg`, `Im008_1.jpg`, `Im009_1.jpg`, `Im010_1.jpg`, `Im011_1.jpg`, `Im012_1.jpg`, `Im013_1.jpg`, `Im014_1.jpg`, `Im016_1.jpg`, `Im017_1.jpg`, `Im019_1.jpg`, `Im023_1.jpg`, `Im026_1.jpg`, `Im028_1.jpg`.

Assessment: the arrows correlate with positive labels and appear near cells, creating a risk that the model will learn artificial cues instead of cell characteristics. **The selected processing plan retains all 15 images with arrows and preserves their pixels.** The presence of these marks will be documented in the dataset and considered when interpreting evaluation results.

### 3. One Pair of Exact Duplicate Images

`Im093_0.jpg` and `Im108_0.jpg` have identical file SHA-256 hashes and identical decoded RGB data. **The working copy retains `Im093_0.jpg` and excludes `Im108_0.jpg`.** This prevents duplicate sampling and avoids placing the same image in different splits. The original source folder remains unchanged.

A near-duplicate search using pHash and grayscale image correlation returned only this pair at the thresholds used. This check does not rule out images with overlapping fields of view or images from the same slide or patient.

### 4. Image Quality and the Risk of Image Source Bias

Thumbnails of all 108 samples and crops at the original resolution were reviewed. `Im094_0.jpg` and `Im095_0.jpg` appear soft or blurry, have low contrast, and fall among the images with the lowest sharpness scores. These two images should be reviewed when preparing the dataset; there is not enough evidence to exclude them automatically based on a sharpness threshold alone.

![Image regions at the original resolution](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_focus_review.jpg)

The score shown in the figure is the Laplacian variance after resizing the image to a maximum long side of 640 pixels. It helps identify images for review; cell count, magnification, and image content also affect the score. For example, `Im017_1.jpg` has a low score, but the annotated cells remain clearly visible, so it should not automatically be considered unusable.

The distribution of image dimensions is associated with the labels:

| Dimensions | `_1` group | `_0` group |
|---|---:|---:|
| 1712 × 1368 | 33 | 0 |
| 2592 × 1944 | 16 | 58 |
| 1226 × 652 | 0 | 1 |

Assessment: differences in magnification, staining color, and image source may create secondary cues. Performance should be checked on independent data, and splits should be made by patient or slide when that information is available. The README file and image filenames do not provide a patient ID mapping. If images are divided into tiles, all tiles from the same source image must remain in the same split.

## Selected image processing and relabeling workflow

### Image selection

All 15 images containing arrows will be retained without cropping, masking, or pixel changes. Exact duplicate images will be removed from the working copy: `Im093_0.jpg` is retained, while `Im108_0.jpg` is excluded. This yields **107 unique images: 49 positive and 58 negative images**, with all **510 annotated blast centroids** retained. Images flagged for quality review remain in the working copy.

The source `ALL_IDB1` folder is preserved. The converter writes a separate workspace containing unchanged image copies and new annotations.

### Convert centroid coordinates into X-AnyLabeling points

Each nonempty row in an `.xyc` file is converted to one native X-AnyLabeling point/keypoint shape:

- `label`: `blast_center`.
- `shape_type`: `point`.
- `points`: `[[x, y]]` in original image pixel coordinates.
- `group_id`: a unique integer for each cell within its image.

The imported coordinates are preserved as supplied: they are not normalized, resized, swapped, or shifted by default. The converter provides `--one-based-input` only for data whose coordinate origin is explicitly documented as one-based; this option was not used for the current conversion.

Each JSON has the same filename stem as its image and is stored beside it. Images without blast cells receive a valid JSON with an empty `shapes` list. This layout follows the [native annotation schema](https://github.com/CVHub520/X-AnyLabeling/blob/main/anylabeling/views/labeling/schema.py) and [JSON loading behavior](https://github.com/CVHub520/X-AnyLabeling/blob/main/anylabeling/views/labeling/label_file.py).

These points are **reference keypoint annotations for relabeling**. They are not a complete YOLO pose training dataset: a YOLO pose instance also needs a bounding box. No pose model is run and no box size is inferred from the centroid alone.

### Relabel the cells as YOLO detection objects

1. Open the converted `images/` folder in X-AnyLabeling. Matching JSON files load the `blast_center` points.
2. Use each point to locate the corresponding blast cell and draw a rectangle labeled `blast` around the visible cell extent. Assign the rectangle the same `group_id` as its reference point to keep the association explicit. If a cell boundary is ambiguous, flag it for review rather than guessing a fixed-size box.
3. Check that each reference point has a corresponding reviewed rectangle and that the rectangle encloses the intended cell. Keep the reference points in the master JSON files for traceability. Retain the negative images without blast rectangles.
4. Export the completed rectangles using **Export Annotations → Export YOLO Annotations → Detection/HBB**, with `classes.txt` containing only `blast`. The official [conversion code](https://github.com/CVHub520/X-AnyLabeling/blob/main/anylabeling/views/labeling/label_converter.py) selects rectangle shapes for detection export, so reference points are not written as detection objects. See the [X-AnyLabeling export guide](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/user_guide.md#41-yolo-format).
5. Verify the exported images and labels, including all negative images. Every detection row should have the form `0 x_center y_center width height`, with normalized coordinates. The `0` is the zero-based class ID for `blast`, not the `_0/_1` image-level suffix. Split the final dataset after relabeling while keeping related source images together.

### Python converter and prepared files

The proposed converter is [ALLIDB1_relabeling.py](https://github.com/raven-172/ALL-Det_raven172/blob/main/dataset/ALLIDB1_relabeling.py). It requires Python and Pillow. It checks coordinate syntax and bounds, verifies image readability, checks duplicate annotation consistency, skips exact duplicate files using SHA-256, and verifies that copied images remain byte-identical. It refuses to overwrite a nonempty output directory to protect manual annotation work.

To create another workspace, run:

```bash
python3 /Users/le/Documents/Codex/2026-10-07/hya/outputs/xyc_to_xanylabeling_points.py \
  --dataset /your_sources_of_your_dataset/
  --output /your_place_you_want_to_save_output/
```

Add `--dry-run` to validate the data and display the counts without writing files.

The converter has already produced a working copy with **107 unchanged images, 107 JSON files, and 510 `blast_center` points**. It excludes only the known exact duplicate `Im108_0.jpg`; the 15 images with arrows are retained. No detection rectangles have been created yet.

- [Prepared point annotation workspace](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_xanylabeling_points/README.md)
- [Example annotation: Im001_1.json](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_xanylabeling_points/images/Im001_1.json)
- [Conversion manifest and counts](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_xanylabeling_points/conversion_manifest.json)

## Scope and evidence

The original audit was read-only and covered JPEG verification, full image decoding with Pillow, image dimensions, color modes and EXIF orientation, file and pixel hash comparisons, coordinate file checks, arrow detection, and visual inspection. The subsequent conversion created a separate annotation workspace without modifying the source dataset. All output coordinates, instance groups, image copies and counts were checked. Native point JSON compatibility was checked against the official X-AnyLabeling source; loading in the installed GUI and manual rectangle relabeling have not been performed. Image validity checks were compared with the [Ultralytics data verification utilities](https://docs.ultralytics.com/reference/data/utils). The Ultralytics library was not installed, the actual YOLO data loader was not invoked, and no training was run. This report assesses the input data, not model performance.

- [Detailed audit results (JSON)](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_audit_details.json)
- [Contact sheet 1: Im001–Im036](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_contact_sheet_1.jpg)
- [Contact sheet 2: Im037–Im072](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_contact_sheet_2.jpg)
- [Contact sheet 3: Im073–Im108](/Users/le/Documents/Codex/2026-10-07/hya/outputs/ALL_IDB1_contact_sheet_3.jpg)

The red crosses on the contact sheets were added for this report to illustrate the positions recorded in the `.xyc` files. These crosses are absent from the source images; the yellow arrows with pink outlines are embedded in the source images.

## Per-image results

`_1`: blast cells present; `_0`: no blast cells. “Blurred: review required” flags an image quality concern, not a decoding error.

| Image filename | Dimensions | Image label | Blast centroid count | Decoding | Notes |
|---|---|---:|---:|---|---|
| Im001_1.jpg | 1712 × 1368 | 1 | 8 | Pass | — |
| Im002_1.jpg | 1712 × 1368 | 1 | 8 | Pass | Arrow embedded in the source image |
| Im003_1.jpg | 1712 × 1368 | 1 | 11 | Pass | — |
| Im004_1.jpg | 1712 × 1368 | 1 | 6 | Pass | — |
| Im005_1.jpg | 1712 × 1368 | 1 | 23 | Pass | — |
| Im006_1.jpg | 1712 × 1368 | 1 | 15 | Pass | — |
| Im007_1.jpg | 1712 × 1368 | 1 | 5 | Pass | Arrow embedded in the source image |
| Im008_1.jpg | 1712 × 1368 | 1 | 15 | Pass | Arrow embedded in the source image |
| Im009_1.jpg | 1712 × 1368 | 1 | 6 | Pass | Arrow embedded in the source image |
| Im010_1.jpg | 1712 × 1368 | 1 | 11 | Pass | Arrow embedded in the source image |
| Im011_1.jpg | 1712 × 1368 | 1 | 13 | Pass | Arrow embedded in the source image |
| Im012_1.jpg | 1712 × 1368 | 1 | 11 | Pass | Arrow embedded in the source image |
| Im013_1.jpg | 1712 × 1368 | 1 | 10 | Pass | Arrow embedded in the source image |
| Im014_1.jpg | 1712 × 1368 | 1 | 3 | Pass | Arrow embedded in the source image |
| Im015_1.jpg | 1712 × 1368 | 1 | 15 | Pass | — |
| Im016_1.jpg | 1712 × 1368 | 1 | 15 | Pass | Arrow embedded in the source image |
| Im017_1.jpg | 1712 × 1368 | 1 | 2 | Pass | Arrow embedded in the source image |
| Im018_1.jpg | 1712 × 1368 | 1 | 5 | Pass | — |
| Im019_1.jpg | 1712 × 1368 | 1 | 11 | Pass | Arrow embedded in the source image |
| Im020_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im021_1.jpg | 1712 × 1368 | 1 | 2 | Pass | — |
| Im022_1.jpg | 1712 × 1368 | 1 | 2 | Pass | — |
| Im023_1.jpg | 1712 × 1368 | 1 | 5 | Pass | Arrow embedded in the source image |
| Im024_1.jpg | 1712 × 1368 | 1 | 3 | Pass | — |
| Im025_1.jpg | 1712 × 1368 | 1 | 2 | Pass | — |
| Im026_1.jpg | 1712 × 1368 | 1 | 4 | Pass | Arrow embedded in the source image |
| Im027_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im028_1.jpg | 1712 × 1368 | 1 | 1 | Pass | Arrow embedded in the source image |
| Im029_1.jpg | 1712 × 1368 | 1 | 2 | Pass | — |
| Im030_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im031_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im032_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im033_1.jpg | 1712 × 1368 | 1 | 1 | Pass | — |
| Im034_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im035_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im036_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im037_0.jpg | 1226 × 652 | 0 | 0 | Pass | Different aspect ratio; still valid |
| Im038_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im039_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im040_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im041_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im042_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im043_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im044_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im045_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im046_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im047_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im048_1.jpg | 2592 × 1944 | 1 | 16 | Pass | — |
| Im049_1.jpg | 2592 × 1944 | 1 | 13 | Pass | — |
| Im050_1.jpg | 2592 × 1944 | 1 | 12 | Pass | — |
| Im051_1.jpg | 2592 × 1944 | 1 | 17 | Pass | — |
| Im052_1.jpg | 2592 × 1944 | 1 | 23 | Pass | — |
| Im053_1.jpg | 2592 × 1944 | 1 | 32 | Pass | — |
| Im054_1.jpg | 2592 × 1944 | 1 | 10 | Pass | — |
| Im055_1.jpg | 2592 × 1944 | 1 | 20 | Pass | — |
| Im056_1.jpg | 2592 × 1944 | 1 | 12 | Pass | — |
| Im057_1.jpg | 2592 × 1944 | 1 | 11 | Pass | — |
| Im058_1.jpg | 2592 × 1944 | 1 | 21 | Pass | — |
| Im059_1.jpg | 2592 × 1944 | 1 | 31 | Pass | — |
| Im060_1.jpg | 2592 × 1944 | 1 | 11 | Pass | — |
| Im061_1.jpg | 2592 × 1944 | 1 | 21 | Pass | — |
| Im062_1.jpg | 2592 × 1944 | 1 | 20 | Pass | — |
| Im063_1.jpg | 2592 × 1944 | 1 | 20 | Pass | — |
| Im064_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im065_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im066_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im067_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im068_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im069_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im070_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im071_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im072_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im073_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im074_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im075_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im076_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im077_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im078_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im079_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im080_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im081_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im082_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im083_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im084_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im085_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im086_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im087_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im088_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im089_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im090_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im091_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im092_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im093_0.jpg | 2592 × 1944 | 0 | 0 | Pass | Duplicate copy: Im108_0.jpg |
| Im094_0.jpg | 2592 × 1944 | 0 | 0 | Pass | Blurred: review required |
| Im095_0.jpg | 2592 × 1944 | 0 | 0 | Pass | Blurred: review required |
| Im096_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im097_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im098_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im099_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im100_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im101_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im102_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im103_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im104_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im105_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im106_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im107_0.jpg | 2592 × 1944 | 0 | 0 | Pass | — |
| Im108_0.jpg | 2592 × 1944 | 0 | 0 | Pass | Exact duplicate of Im093_0.jpg |
