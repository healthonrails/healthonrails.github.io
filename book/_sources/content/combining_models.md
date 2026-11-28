# Combining Models & Multi-Tool Pipelines

One of Annolid's biggest strengths is that every model — whether SAM, Cutie, SAM3, DINOv3, INSID3, YOLO, or an imported DeepLabCut/SLEAP file — reads and writes the **same open LabelMe JSON / NDJSON and CSV data contracts**. You can mix and match the fastest tool for each stage instead of getting locked into one model.

```{figure} ../images/diagrams/choose_your_tracker.png
---
name: combine-choose-tracker
alt: Decision matrix comparing Cutie VOS, SAM3, DINOv3 Keypoints, INSID3, YOLO, and Sim-to-Real Studio
width: 96%
---
Each Annolid AI backend specializes in a different link of the pipeline — combine them freely on the same video folder.
```

## Proven Multi-Model Recipes

### Recipe 1: SAM AI-Polygons → Cutie or SAM3 → Automated Track QC
*Best everyday pipeline for 1–5 animals with zero training.*

1. Outline each animal on frame 0 with **Create AI-Polygon** (EfficientSAM / SAM2).
2. Propagate masks across the video using **[Cutie](tracking_with_Cutie.md)** or **[SAM3](../tutorials/SAM3_video_tracking.md)**.
3. Run **[Track QC](../tutorials/Reporting_and_track_qc.md)** (`annolid-run track-qc`) to find any 5-frame occlusion dropout, fix that single anchor frame, and resume.

### Recipe 2: Whole-Body Masks + Sparse Body-Part Keypoints
*Best for social investigation, nose-to-anogenital contact, and head-direction analysis.*

1. Track whole-animal silhouettes (`resident`, `intruder`) with **Cutie** or **SAM3**.
2. Place anatomical seed points (`nose`, `left_ear`, `right_ear`, `tail_base`) on frame 0 and propagate them constrained inside each animal's mask using **[DINOv3 Keypoint Tracking](../tutorials/DINOv3_keypoint_tracking.md)**.
3. Run `annolid-run body-part-ethogram` or `annolid-run report` to automatically quantify directed nose-to-body contact bouts!

### Recipe 3: Hierarchical Body-Part Segmentation (Head / Torso / Tail)
*Best when you want pixel-accurate body-part masks with zero cross-animal identity bleed.*

```{figure} ../images/showcase/sim_body_part_segmentation.png
---
name: combine-body-parts
alt: Side-by-side 3D ground truth vs Annolid predicted hierarchical body-part segmentation on resident-intruder mice
width: 94%
---
Hierarchical body-part segmentation decomposes tracked whole-animal masks into clean `head`, `torso`, and `tail` sub-regions while preserving individual identity.
```

- Start from tracked whole-animal polygons (`Cutie` / `SAM3`), then segment non-overlapping anatomical sub-parts per instance (see the [Instance Body Part Segmentation Guide](https://annolid.com/portal/body_part_segmentation/) on the Docs Portal).

### Recipe 4: Text Prompts → Curated Dataset → Custom YOLO11 / YOLO26
*Best for scaling from one annotated video to a 100-video cohort.*

1. Bootstrap initial masks with **Grounding DINO → SAM** or **SAM3 text prompts**.
2. Clean up 30–100 diverse frames in the Annolid GUI.
3. Fine-tune a fast **YOLO11 / YOLO26** model locally or on **[Google Colab](Annolid_on_Google_Colab.md)**, then run batch inference across all remaining recordings and review only frames flagged by **Track QC**.

### Recipe 5: Sim-to-Real 3D Bootstrap + Real Label Mixing
*Best when you have new arenas/lighting and want to avoid labeling from scratch.*

1. Generate environment-matched synthetic pose or body-part frames in **[Sim-to-Real Studio](../tutorials/Simulation_3d_digital_twins.md)**.
2. Mix in 10–20 real corrected LabelMe frames from your own recordings during Iteration 2 for rapid domain adaptation.

## Choosing Your Source-of-Truth Format

| Format | Keep As Source Of Truth When… |
| --- | --- |
| **LabelMe JSON + `*_annotations.ndjson`** | You are still reviewing, editing polygons/keypoints, or re-tracking segments inside Annolid. |
| **`*_tracked.csv` + `*_events.csv`** | You are running statistics, zone occupancy, kinematics, or custom plotting in Python / R. |
| **COCO / YOLO / DeepLabCut / SLEAP** | You are training external models or collaborating with labs using those toolchains. |
