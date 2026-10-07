# ALL-IDB1 Dataset

Documentation and processing tools for single-class `blast` detection.

**Status:** Dataset review and manual reannotation completed on 7 October 2026.

## Initial Dataset

- **108 JPEG images:** 49 positive images and 59 negative images.
- **108 matching `.xyc` files:** 510 blast-center annotations, with no bounding-box dimensions.
- **Review findings:** one exact duplicate (`Im108_0.jpg` duplicates `Im093_0.jpg`) and 15 positive images with embedded arrows.

Center coordinates alone were insufficient for YOLO detection, so the target cells required manual bounding-box annotation.

## Processing and Reproduction

1. Obtain ALL-IDB1 through the [official dataset instructions](https://scotti.di.unimi.it/all/). The source folder must contain `im/` for images and `xyc/` for centroid files.
2. From the repository root, install Pillow and run the [preparation script](ALLIDB1_relabeling.py):

   ```bash
   python3 -m pip install Pillow
   python3 dataset/ALLIDB1_relabeling.py \
     --dataset /path/to/ALL_IDB1 \
     --output dataset_relabel/ALL_IDB1
   ```

   Use a new or empty output folder outside the source dataset. Add `--dry-run` to validate without writing files. The script excludes exact duplicates and creates unchanged image copies with `blast_center` reference points in native JSON; bounding boxes are drawn manually.
3. Open the output `images/` folder in [X-AnyLabeling](https://github.com/CVHub520/X-AnyLabeling). Draw a rectangle labeled `blast` around each referenced cell, review its visible boundaries, and save the JSON annotations. Retain negative images without blast rectangles.
4. To prepare training labels, export reviewed rectangles through **Export Annotations → Export YOLO Annotations**, selecting the **Detection** task (horizontal bounding boxes) and using the generated `classes.txt` containing only `blast`. Retain negative images with empty labels and check normalized rows of the form `0 x_center y_center width height`. See the [export guide](https://github.com/CVHub520/X-AnyLabeling/blob/main/docs/en/user_guide.md#41-yolo-format) and [YOLO detection format](https://docs.ultralytics.com/datasets/detect/).

## Final Results

| Item | Result |
| --- | --- |
| Unique images | **107**: 49 positive and 58 negative |
| Images processed | **107/107 (100%)** |
| Original blast-center references | 510 |
| Center-to-bounding-box conversion | **100% completed** |
| Annotation class and format | `blast` rectangles in native JSON |
| Image handling | One duplicate excluded; source pixels preserved, including embedded arrows |

Manual reannotation is complete. The completed annotation workspace is maintained locally; this folder provides the documentation and preparation tools. Embedded arrows remain relevant when interpreting model performance.

### Quick Links

- [Initial dataset assessment](Dataset-assessment.md) — archived inspection before manual reannotation.
- [Processing log and before/after screenshots](../log_book/LOG002_Dataset-Processing.md).
- [Dataset preparation script](ALLIDB1_relabeling.py).
- [ALL-IDB application form (PDF)](form_ALL-IDB.pdf).
