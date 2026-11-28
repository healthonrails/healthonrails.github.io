# Built-in Models & Annolid ModelZoo

Annolid ships with — or automatically downloads on first use — a broad library of foundation segmentation, tracking, keypoint, depth, and object-detection backends, alongside community example datasets and pretrained weights.

If you have an annotated behavioral dataset or trained model you would like to share with the research community, please [get in touch](get_in_touch.md).

## Built-in AI Model Backends

| Model Family | Task | Training Needed? | Typical Starting Point |
| --- | --- | --- | --- |
| **EfficientSAM / SAM2** | Interactive AI-Polygons from point clicks | No | Fast frame-0 seeding on CPU or GPU |
| **Grounding DINO → SAM** | Text-prompted bounding boxes + masks | No | Bootstrapping masks from text labels |
| **Cutie VOS** | Multi-animal video mask tracking | No (1 seed frame) | Everyday 1–5 animal tracking |
| **SAM3 / SAM3 Agent** | Long-video tracking, text prompts & occlusion repair | No | Long videos, re-entries, NDJSON correction |
| **DINOv3 Keypoint Tracker** | Sparse anatomical body-part tracking | No (seed points) | Nose, ears, hips, tail base (`rodent_30fps` / `fly_70fps`) |
| **INSID3 Video (DINOv3)** | In-context frame-independent segmentation | No (1 reference frame) | Clean DINOv3 masks stored in NDJSON |
| **TAPNext / CoWTracker** | Dense & sparse ONNX/PyTorch point tracking | No | Alternative point-tracking backends |
| **YOLO11 / YOLO26 / YOLOE** | Detection, instance seg & pose estimation | Optional (or pretrained) | High-throughput cohorts & real-time cameras |
| **Video Depth Anything** | Temporally consistent per-frame depth maps | No | 2D→3D lifting, rearing height, point clouds |

Most checkpoints download automatically on first use via standard Hugging Face or Ultralytics caches (or can be prefetched with `annolid-run dinov3-models` and `python -m annolid.depth.download_weights`).

## Example Annotated Dataset (COCO Format)

An example behavioral dataset annotated with Annolid and exported to COCO format is available on Google Drive:

- [Download example COCO dataset (Google Drive)](https://drive.google.com/file/d/1fUXCLnoJ5SwXg54mj0NBKGzidsV8ALVR/view?usp=sharing)

```{figure} ../images/novelctrlk6_8_coco_dataset_example.jpg
---
name: zoo-coco-example
alt: Example annotated frame from the Annolid COCO sample dataset
width: 78%
---
Sample annotated frame from the shared Annolid COCO example dataset.
```

## Example Pretrained Models

Pretrained model weights corresponding to the example datasets are available here:

- [Browse shared pretrained models (Google Drive folder)](https://drive.google.com/drive/folders/1t1eXxoSN2irKRBJ8I7i3LHkjdGev7whF?usp=sharing)

## Sharing Your Own Models With the Community

To make a shared model effortless for other labs to run without retraining, include:

1. a small sample dataset (LabelMe JSON, COCO, or YOLO export),
2. the trained checkpoint weights (noting model family, task, and recommended image size), and
3. a short README listing exact class/keypoint names and camera setup notes.
