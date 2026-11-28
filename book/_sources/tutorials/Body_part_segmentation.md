# Hierarchical Instance Body-Part Segmentation

Standard video trackers follow an animal's **whole body** (`mouse_1`, `mouse_2`). **Instance Body Part Segmentation** goes one level deeper: it decomposes each tracked parent polygon into non-overlapping anatomical sub-regions — such as `head`, `torso`, `tail`, limbs, snout, or wings — **strictly inside each animal's own ROI**.

```{figure} ../images/diagrams/body_part_segmentation_pipeline.png
---
name: body-parts-pipeline
alt: Four-stage hierarchical body-part segmentation pipeline from tracked parent ROIs through canonical pose frame and mode selection to disjoint part outputs
width: 100%
---
Every animal is segmented independently inside its own hard-masked parent crop — preventing cross-animal bleed even during tight social huddles.
```

## Why Hierarchical Body-Part Segmentation?

- **Zero cross-animal bleed**: Pixels outside a parent animal's mask are strictly excluded, even during nose-to-body investigation or mounting.
- **Merged-parent huddle recovery**: When two animals temporarily merge into one parent blob, edge-weighted geodesic + Lab color splitting separates them and freezes prototype drift.
- **Disjoint sub-parts**: Sibling parts inside one animal never overlap (`head`, `torso`, `tail` partition cleanly).
- **360° coiled-posture invariance**: Uses a pose-normalized body frame with an intrinsic masked geodesic spine so C-shaped, U-shaped, and coiled animals stay cleanly oriented.

```{figure} ../images/showcase/sim_body_part_segmentation.png
---
name: body-parts-benchmark-preview
alt: Side-by-side comparison of 3D ground truth vs Annolid predicted head, torso, and tail body-part segmentation
width: 96%
---
Ground-truth 3D anatomical parts vs. Annolid hierarchical body-part predictions on interacting resident-intruder mice.
```

## Choose Your Mode & Feature Backbone

| Mode (`--mode`) | Inputs Required | Best For |
| --- | --- | --- |
| **`auto`** *(default)* | Tracked parent polygons (+ optional seed parts or keypoints) | Picks `seeded` if part polygons exist, `keypoint_guided` if keypoints exist, or `unsupervised` otherwise. |
| **`seeded`** | Manual part polygons drawn on 1+ seed frames (one animal is enough!) | Custom parts (`snout`, `ear`, `head`, `torso`, `tail`) or partial labeling (`head` only). |
| **`keypoint_guided`** | Tracked parent polygons + sparse keypoints (DINOv3, YOLO-Pose, TAPNext) | Turning sparse skeletons into dense anatomical masks without drawing part polygons. |
| **`unsupervised`** | Tracked parent polygons only | Fast axial decomposition (`anterior`/`posterior` or `head`/`torso`/`tail`) with zero supervision. |

| Backbone (`--backbone`) | Speed & Dependencies | When to Pick |
| --- | --- | --- |
| **`fast`** *(default)* | ~1–3 ms/crop on CPU (OpenCV + NumPy only) | Everyday default for long recordings and laptops. |
| **`dino`** | PyTorch + `transformers` (DINOv3 ViT patch features) | Strongest semantic invariance across coat patterns or lighting shifts. |
| **`hybrid`** | DINOv3 semantics + high-resolution Lab/gradient edges | Sharpest boundaries + stability on CUDA / Apple Silicon MPS. |

## Run in GUI, CLI, or Python

::::{tab-set}

:::{tab-item} Desktop GUI
1. Track your whole animals first (with **[Cutie](../content/tracking_with_Cutie.md)**, **[SAM3](SAM3_video_tracking.md)**, or **YOLO**).
2. *(Optional, for `seeded` mode)* Draw body-part polygons (`head`, `torso`, `tail`) inside **one** animal on a clear frame and press `Ctrl+S` — prototypes automatically share across other animals of the same species.
3. Choose **`Instance Body Part Segmentation`** in the top **AI Model** dropdown and click **`Pred`**.
:::

:::{tab-item} CLI (`annolid-run`)
```bash
# Fast CPU auto mode + CSV export
annolid-run segment-body-parts /path/to/social_assay.mp4 \
  --mode auto \
  --backbone fast \
  --export-csv

# Keypoint-guided fine body parts using a PoseSchema
annolid-run segment-body-parts /path/to/fly_courtship.mp4 \
  --annotations /path/to/fly_courtship \
  --mode keypoint_guided \
  --keypoint-granularity fine \
  --pose-schema /path/to/pose_schema.yaml \
  --export-csv

# Seeded mode with hybrid DINOv3 + Lab/gradient features
annolid-run segment-body-parts /path/to/session.mp4 \
  --mode seeded \
  --backbone hybrid \
  --dino-model facebook/dinov3-vits16-pretrain-lvd1689m \
  --qualify-labels \
  --out /path/to/session/body_part_report.json
```
:::

:::{tab-item} Python API
```python
from annolid.segmentation import (
    BodyPartSegmentationConfig,
    InstanceBodyPartVideoProcessor,
)

config = BodyPartSegmentationConfig(
    mode="auto",
    feature_backend="fast",
    crop_size=224,
    guided_radius=4,
    split_merged_parent_masks=True,
)
processor = InstanceBodyPartVideoProcessor(
    "/path/to/video.mp4",
    results_folder="/path/to/video",
    body_part_config=config,
)
summary = processor.process_video_frames(start_frame=0)
processor.cleanup()
print(summary)
```
:::

::::

## Bonus: Compact `Cutie (SAM3 Body Parts)` Distilled Tracker

Prefer direct VOS propagation of both whole animals and body parts in a single Cutie pass? Select **`Cutie (SAM3 Body Parts)`** in the model dropdown:

- Dual-teacher distilled (`SAM 3.1` + `DINOv3 ViT-L/16`) and compressed **4.43× smaller** (`133.9 MB → 30.3 MB`, **55% fewer parameters**).
- Runs **1.48× faster on CPU** and up to **2.72× faster on Apple Silicon MPS**, while raising held-out body-part `J&F` from `0.780` to `0.813`.
- Original **`Cutie`** remains untouched as the default for strict backward compatibility.

```{tip}
Want deeper parameter tuning (`--partial-parts`, `--num-parts`, `--no-split-merged-parents`)? See the full [Instance Body Part Segmentation Guide](https://annolid.com/portal/body_part_segmentation/) on the Docs Portal.
```
