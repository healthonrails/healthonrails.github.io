# How Annolid Works (Technical Overview)

Whether you are labeling a single 2-minute clip or analyzing a 100-video cohort, Annolid follows one clean, reviewable five-stage loop — with human-in-the-loop checkpoints at every step so you always know what happened and can fix mistakes in seconds.

```{figure} ../images/diagrams/annolid_modern_workflow.png
---
name: overview-modern-workflow
alt: Five-stage Annolid pipeline from Prepare and Seed & Label through Track & Pose, Review & QC, to Analyze & Report, backed by Annolid Bot, 3D Twins, and open data formats
width: 100%
---
Annolid's end-to-end research pipeline: open videos directly, seed one frame, propagate with foundation or custom models, audit with Track QC, and export reproducible reports.
```

## The Five-Stage Loop

1. **Prepare**: Open your video directly in the GUI (`File → Open Video`) — frame extraction is optional. For large folders of high-resolution videos, use [Downsample & Crop](downsample_and_crop_videos.md) to speed up interactive playback and inference.
2. **Seed & Label**: Navigate to a clean representative frame and annotate your targets using **SAM AI-Polygons**, **text prompts** (Grounding DINO → SAM or SAM3), **keypoints**, **spatial zones**, and **behavior flags**.
3. **Track & Pose**: Propagate labels forward (or across segments) using a training-free tracker (**Cutie**, **SAM3**, **DINOv3 Keypoints**, **INSID3**) or run a trained **YOLO11 / YOLO26 / YOLOE** model locally or on Google Colab.
4. **Review & Track QC**: Run automated **Track QC** to surface missing frames, occlusion dropouts, velocity spikes, and identity swaps. Jump straight to the first error frame, fix one anchor mask, and re-propagate cleanly.
5. **Analyze & Report**: Compute spatial zone occupancy, calibrated kinematics, freezing bouts, ethogram time budgets, inter-rater reliability (IRR), and cohort statistics — exported as plain CSV/JSON plus a self-contained **HTML5 + inline SVG report**.

```{figure} ../images/diagrams/human_in_the_loop_animation.gif
---
name: overview-hitl-animation
alt: Animated 4-stage diagram showing Seed Frame, Auto-Track Forward, Spot Occlusion with Track QC, and Fix Anchor & Re-Propagate
width: 96%
---
Annolid's human-in-the-loop tracking cycle: correct only the frames that actually need help instead of relabeling entire videos.
```

## Choosing the Right AI Backend

Not every project needs custom model training. Use the guide below to pick the fastest path for your recording:

```{figure} ../images/diagrams/choose_your_tracker.png
---
name: overview-choose-tracker
alt: Six-card decision guide comparing Cutie VOS, SAM3 / SAM3 Agent, DINOv3 Keypoints, INSID3 Video, YOLO11/26/YOLOE, and Sim-to-Real Studio
width: 100%
---
Quick decision guide for choosing between training-free trackers, custom fine-tuned models, and 3D Sim-to-Real bootstrapping.
```

### Path A: Track from one frame (zero training — best starting point)
- Label 1 clean seed frame with **AI-Polygons** (SAM clicks) or **text prompts**.
- Propagate masks across the video using **[Cutie](tracking_with_Cutie.md)**, **[SAM3](../tutorials/SAM3_video_tracking.md)**, or **[INSID3](../tutorials/INSID3_video_segmentation.md)**.
- Add sparse body-part landmarks (nose, ears, tail base) with **[DINOv3 Keypoint Tracking](../tutorials/DINOv3_keypoint_tracking.md)**.

### Path B: Train a fast reusable model (best for large cohorts & real-time)
- Export ~20–150 corrected LabelMe frames (or an existing COCO dataset) to YOLO format.
- Fine-tune **YOLO11 / YOLO26** segmentation, detection, or pose models via the **Training Wizard** locally or on **[Google Colab](Annolid_on_Google_Colab.md)**.
- Monitor curves and compare runs in the built-in **Training Monitor (`Ctrl+Shift+V`)**.

### Path C: Bootstrap with 3D Digital Twins (zero manual labels)
- Point **[Sim-to-Real Studio](../tutorials/Simulation_3d_digital_twins.md)** at raw example videos of your arena.
- Annolid matches lighting, arena geometry, and species in its bundled offline Three.js 3D simulator, generates labeled pose or body-part datasets, trains on Colab or locally, and evaluates back on your real videos.

## Open, Reviewable File Formats

Annolid never locks your work into opaque binary databases:

| Artifact | Format | Purpose |
| --- | --- | --- |
| Manual seed frames & edits | `<video>_#########.json` (LabelMe JSON) | Human-readable polygons, keypoints, zones, and flags |
| High-volume predicted frames | `<video>_annotations.ndjson` (`AnnotationStore`) | Fast append-only storage without creating 50,000 tiny files |
| Frame-by-frame tracking tables | `*_tracking.csv` & `*_tracked.csv` | RLE masks, bounding boxes, centroids, speed, and zone columns |
| Behavior schema & ethograms | `project.annolid.json` & `*_events.csv` | Shared across Flags, Timeline, Annolid Bot, and BORIS I/O |
| External ecosystem exchange | COCO JSON, YOLO `data.yaml`, DeepLabCut CSV/H5, SLEAP `.slp`/`.h5` | Seamless round-trips with other lab pipelines |

## Practical Performance Tips

- **Downsample before tracking**: Scaling 4K or 1080p footage to ~640–960 px wide dramatically improves Cutie, SAM3, and DINOv3 speed with minimal accuracy loss for most behavioral arenas.
- **Keep `annolid[gui]` lean**: Annolid starts quickly with a minimal GUI footprint and installs optional ML/tracking runtimes on demand (or upfront via `--profile tracking` / `--profile workstation`).
- **Use hardware acceleration when available**: Annolid automatically selects NVIDIA CUDA, Apple Silicon MPS, or CPU, and offloads heavy training to **Google Colab** when you only have a laptop.

Ready to install? Continue to [Installation Options](how_to_install.md).
