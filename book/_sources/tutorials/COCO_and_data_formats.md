# Data Formats & COCO / YOLO / NDJSON Cookbook

Annolid is built on transparent, open file formats so your research annotations stay readable and reusable years later — whether you train in Ultralytics YOLO, PyTorch, Detectron2, DeepLabCut, SLEAP, or analyze in Python and R.

## Dual Annotation Storage (Manual JSON + Fast NDJSON)

When working with long videos, Annolid balances human editability with filesystem speed using **two complementary layers** inside `<video_stem>/`:

| Layer | Filename Pattern | Purpose |
| --- | --- | --- |
| **Manual seeds & edits** | `<video_stem>_000000000.json` + `.png` | Human-edited frames, anchor seeds, and zones. Supersede automatic predictions during re-tracking. |
| **High-volume predictions** | `<video_stem>_annotations.ndjson` | Append-only `AnnotationStore` writing thousands of tracked frames cleanly into a single file instead of 50,000 tiny files. |

All Annolid export, Track QC, zone, pose, and reporting tools read **both** layers automatically so you never have to merge them manually.

## Shared COCO Data Flow (Zero Manual YAML Required)

Annolid uses one unified COCO layer across **YOLO**, **DINO KPSEG**, **Keypoint R-CNN**, and **Mask R-CNN**. You can point the **Training Wizard** or `annolid-run` directly at any of these:

- a COCO dataset root containing an `annotations/` folder (`instances_train.json`, `person_keypoints_train.json`, `train.json`),
- split-local folders (`train/annotations.json`, `val/annotations.json`) with images sitting alongside each JSON, or
- an explicit COCO spec YAML:

```yaml
format: coco
path: /path/to/dataset_root
image_root: images
train: annotations/person_keypoints_train.json
val: annotations/person_keypoints_val.json
```

### Automatic Task Detection & Non-Destructive Staging
- **Auto-detects task**: If keypoint metadata is present, Annolid stages a **Pose** dataset (`kpt_shape`, `flip_idx`); otherwise it stages **Segmentation** or **Detection** (supporting polygon lists and compressed/uncompressed RLE masks).
- **Non-destructive**: When training YOLO from COCO, Annolid hardlinks images and materializes a temporary YOLO staging folder without touching your original COCO archive.
- **Auto-validation**: If `val` is omitted from a COCO spec, Annolid can automatically create a validation split and fails fast with a clear message if a pose model is pointed at a detection-only dataset.

## Format Conversion Cheat Sheet

| From → To | GUI Action | CLI Command |
| --- | --- | --- |
| **LabelMe → Tracking CSV** | `File → Save CSV` | `python -m annolid.annotation.labelme2csv --json_folder ./video/` |
| **LabelMe → YOLO dataset** | `File → Convert Labelme to YOLO format` | `annolid-run collect-labels` → `annolid-run index-to-yolo` |
| **LabelMe → COCO** | `File → COCO format` | Use GUI Dataset Export Wizard (supports polygons, masks & keypoints) |
| **DLC / SLEAP → LabelMe** | `Tools → DeepLabCut / SLEAP Import…` | `annolid-run import-pose input.csv --video vid.mp4 -o ./out` |
| **LabelMe / CSV → DLC / SLEAP** | `Tools → DeepLabCut / SLEAP Export…` | `annolid-run export-pose ./out --format sleap-slp --embed-images -o out.pkg.slp` |
| **BORIS ↔ Annolid Events** | `Analysis & Reporting Studio` | `annolid-run boris-import` / `annolid-run boris-export` |

```{tip}
Keep a single `project.annolid.json` and `pose_schema.json` at the root of your lab project so every export locks identical class IDs, keypoint ordering, and skeleton bone definitions. See [COCO Data Flow](https://annolid.com/portal/coco_data_flow/) on the Docs Portal for full YAML specifications.
```
