# The Annolid Book

:::::{container} ann-book-hero
<span class="ann-book-kicker">Interactive Guide · Screenshots · Animations · Real Lab Walkthroughs</span>

<div class="ann-hero-title">Annotate, track, and quantify animal behavior — from raw video to publication-ready figures.</div>

**Annolid** combines a desktop annotation GUI (`annolid`), a reproducible CLI (`annolid-run`), foundation-model tracking (Cutie, SAM3, DINOv3, INSID3, TAPNext, CoWTracker, YOLO), automated Track QC, behavior ethograms, spatial zones, large-TIFF / Brain 3D reconstruction, and offline 3D digital animal simulations in one unified toolkit.

::::{container} ann-cta-row
[Install Annolid in 2 Minutes →](how_to_install.md)
[Featured Walkthrough (mouse083)](../tutorials/mouse083_resident_intruder_showcase.md)
[Track From One Frame](tracking_with_Cutie.md)
[Quick Reference Cheat Sheet](quick_reference_cheatsheet.md)
[Docs Reference Portal](https://annolid.com/portal/)
::::
:::::

[![Annolid CI](https://github.com/healthonrails/annolid/actions/workflows/CI.yml/badge.svg)](https://github.com/healthonrails/annolid/actions/workflows/CI.yml)
[![Release](https://github.com/healthonrails/annolid/actions/workflows/release.yml/badge.svg)](https://github.com/healthonrails/annolid/actions/workflows/release.yml)
[![Publish to PyPI](https://github.com/healthonrails/annolid/actions/workflows/annolid-publish.yml/badge.svg)](https://github.com/healthonrails/annolid/actions/workflows/annolid-publish.yml)

## See Annolid in Action

:::::{container} ann-gallery

::::{container} ann-card
![Animated multi-animal polygon, 14-keypoint skeleton, and behavior tracking demo on mouse083_task1_annotator1](../images/showcase/mouse083_tracking_demo.gif)

:::{container} ann-card-body
<div class="ann-card-title">Multi-Animal Tracking &amp; 14 Keypoints</div>

Follow instance polygons, anatomical skeletons, and live social states across 4,881 frames of real home-cage video.

[Walk through the mouse083 assay →](../tutorials/mouse083_resident_intruder_showcase.md)
:::
::::

::::{container} ann-card
![Annolid desktop GUI displaying polygons, keypoints, Flags dock, and Label Instances](../images/showcase/mouse083_gui_workspace.png)

:::{container} ann-card-body
<div class="ann-card-title">Desktop GUI for Polygons, Keypoints &amp; Flags</div>

Click once with SAM AI-Polygons, scrub the behavior timeline, and inspect synchronized docks in one dark-mode Qt app.

[Learn fast GUI annotation →](labelling_images.md)
:::
::::

::::{container} ann-card
![Ethogram timeline raster, inter-animal proximity curve, arena trajectories, and behavior time budget](../images/showcase/mouse083_ethogram_kinematics.png)

:::{container} ann-card-body
<div class="ann-card-title">Ethograms, Zones, Track QC &amp; HTML5 Reports</div>

Automatically flag occlusion gaps, compute zone occupancy and freezing bouts, and export self-contained HTML5/SVG reports.

[Explore Track QC &amp; Reporting →](../tutorials/Reporting_and_track_qc.md)
:::
::::

::::{container} ann-card
![Offline Three.js 3D Two-Mouse simulation in Fly-Brain LIF Connectome mode](../images/showcase/sim_fly_brain_connectome.png)

:::{container} ann-card-body
<div class="ann-card-title">Offline 3D Digital Twins &amp; Sim-to-Real</div>

Run 10 Two-Mouse 3D arenas, Fly-Brain LIF spiking circuits, Rat NCAP spinal locomotion, and zero-label Sim-to-Real training.

[Explore 3D Simulations →](../tutorials/Simulation_3d_digital_twins.md)
:::
::::

:::::

## Choose Your Path

:::::{container} ann-path-grid

::::{container} ann-path-card
**1. First-Time User (No Training Needed)**

Install Annolid, open a short video directly, outline your animals on frame 0 with AI-Polygons, and track the entire clip with Cutie or SAM3.

[Install](how_to_install.md) · [Label 1 Frame](labelling_images.md) · [Track with Cutie](tracking_with_Cutie.md)
::::

::::{container} ann-path-card ann-path-card--warm
**2. Behavior, Pose & Quantitative Analysis**

Score ethograms on the timeline, draw spatial zones, interoperate with DeepLabCut/SLEAP, audit with Track QC, and export HTML5 reports.

[Zones](../tutorials/Place_preference.md) · [Pose &amp; DLC/SLEAP](../tutorials/Pose_estimation_and_interop.md) · [Track QC &amp; Reports](../tutorials/Reporting_and_track_qc.md)
::::

::::{container} ann-path-card
**3. Cohort Scale, Live Cameras & 3D Twins**

Fine-tune YOLO11/YOLO26 on Colab, run wireless multi-camera detection, search hours of video with EmbeddingGemma 2, or bootstrap from 3D twins.

[Train YOLO](model_training.md) · [Live Cameras](../tutorials/Realtime_and_multicamera.md) · [3D Twins &amp; Sim-to-Real](../tutorials/Simulation_3d_digital_twins.md)
::::

:::::

## How This Book Is Organized

| Part | What You Will Learn | Recommended Starting Chapter |
| --- | --- | --- |
| **Start Here** | What Annolid does, how the pipeline fits together, tabbed installation, lab-bench cheat sheet, and FAQ. | [Introduction](introduction.md) · [Installation](how_to_install.md) · [Cheat Sheet](quick_reference_cheatsheet.md) · [FAQ](troubleshooting_and_faq.md) |
| **Prepare Videos & Annotate** | Batch downsample & crop folders, label polygons/keypoints with SAM clicks or text prompts, merge shapes, and reorder lists. | [Labeling Instances](labelling_images.md) · [GUI Power Tips](../tutorials/GUI_power_tips_and_editing.md) |
| **Tracking, Segmentation & Pose** | Real `mouse083` assay, Cutie, SAM3, segment batch tracking, hierarchical body-part masks, DINOv3, TAPNext, CoWTracker, INSID3, Pose Workbench & DLC/SLEAP interop. | [mouse083 Walkthrough](../tutorials/mouse083_resident_intruder_showcase.md) · [Body-Part Segmentation](../tutorials/Body_part_segmentation.md) · [Pose & DLC/SLEAP](../tutorials/Pose_estimation_and_interop.md) |
| **Behavior, Zones & Analysis** | Place preference, ethogram scoring, TCN behavior classifiers, freezing/optical flow, distances, EmbeddingGemma 2 frame search, Identity Governor, Track QC, IRR, and HTML5 reports. | [Track QC & Reports](../tutorials/Reporting_and_track_qc.md) · [TCN Classifiers](../tutorials/TCN_behavior_classification.md) · [Frame Search & ID Repair](../tutorials/Frame_search_and_identity_repair.md) |
| **Train Models & Scale Up** | Train YOLO11/YOLO26/YOLOE, COCO/YOLO/NDJSON data formats, Google Colab GPUs, batch downsampling, and real-time multi-camera pipelines. | [Model Training](model_training.md) · [COCO & Data Formats](../tutorials/COCO_and_data_formats.md) · [Live Cameras](../tutorials/Realtime_and_multicamera.md) |
| **Microscopy & 3D Digital Twins** | View gigapixel TIFF + Illustrator atlas overlays, reconstruct Brain 3D coronal planes, and explore offline 3D animal twins & Sim-to-Real Studio. | [Large TIFF & Brain 3D](../tutorials/Large_images_and_brain_3d.md) · [3D Twins & Sim-to-Real](../tutorials/Simulation_3d_digital_twins.md) |
| **Automation, CLI & Annolid Bot** | Annolid Bot slash commands (`/track`, `/qc`, `/stats`, `/report`, `/sim2real`), MCP servers, LanceDB Memory, Google/Box integrations, security audits, and `annolid-run` CLI. | [Annolid Bot](prediction_review_agent.md) · [MCP, Memory & Security](../tutorials/Integrations_mcp_cloud_memory.md) · [CLI Reference](Expert_mode_CLI_tools.md) |
| **Resources & Community** | ModelZoo datasets, YouTube tutorials, citation BibTeX, publications using Annolid, contributing, and license. | [ModelZoo](annolid_zoo.md) · [Cite Annolid](cite_annolid.md) |

```{tip}
**Quickest 60-second setup:** Install the lean GUI with `pip install "annolid[gui]"` (or run our [one-line installer](how_to_install.md)), launch `annolid`, and open a video directly — frame extraction is optional!
```

```{note}
**Book vs. Docs Portal:** This book is designed for step-by-step, visual, chapter-style learning. For exhaustive CLI flags, API contracts, MCP/security references, and operational docs, visit the [Annolid Docs Portal](https://annolid.com/portal/).
```
