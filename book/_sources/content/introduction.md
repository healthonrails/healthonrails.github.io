# Introduction

**Annolid** stands for **Annotation + Annelid** (*segmentation*). It is an open-source research platform that brings annotation, instance segmentation, multi-animal tracking, pose keypoints, behavior scoring, quantitative reporting, microscopy/3D brain reconstruction, and 3D digital animal simulations into one cohesive workspace.

<div class="ann-stats">
  <div class="ann-stat">
    <strong>1-Frame Tracking</strong>
    <span>Propagate masks with Cutie, SAM3, or INSID3 with zero model training</span>
  </div>
  <div class="ann-stat">
    <strong>Polygons + Pose</strong>
    <span>Combine whole-body masks, body parts, and anatomical keypoints</span>
  </div>
  <div class="ann-stat">
    <strong>Open Data Contracts</strong>
    <span>LabelMe JSON/NDJSON, CSV, COCO, YOLO, DeepLabCut, SLEAP &amp; BORIS</span>
  </div>
  <div class="ann-stat">
    <strong>GUI + CLI + Bot</strong>
    <span>Interactive Qt app, <code>annolid-run</code> CLI, and Annolid Bot copilot</span>
  </div>
</div>

## What You Can Do With Annolid Today

- **Label faster with AI assistance**: Draw accurate instance masks with a few clicks using **SAM AI-Polygons**, bootstrap masks with **text prompts** (Grounding DINO → SAM or SAM3), and place anatomical keypoints directly on video frames with the **Keypoint Sequencer**.
- **Track multiple animals through occlusions**: Propagate masks from a single labeled frame with **Cutie**, **SAM3**, or **INSID3**, and track sparse body-part landmarks with **DINOv3 Keypoint Tracking**, **TAPNext (ONNX)**, or **CoWTracker**.
- **Review and repair tracks efficiently**: Run automated **Track QC** to pinpoint occlusion gaps, velocity spikes, and identity-swap suspects, jump directly to flagged frames, repair identities with **Identity Governor**, or re-propagate cleanly.
- **Score & search behaviors**: Mark ethogram bouts on the synchronized **Timeline** and **Flags** docks, search hours of video by plain English with **ONNX EmbeddingGemma 2**, run 1-second **Annolid Bot** segment labeling, define reusable **Zones**, and import/export **BORIS** projects.
- **Generate publication-grade analytics**: Compute calibrated kinematics (`px_per_cm` or planar homography), freezing bouts, inter-rater reliability (IRR), cohort statistics, and self-contained **HTML5 + inline SVG reports**.
- **Train custom models, run live cameras & simulate in 3D**: Fine-tune **YOLO11 / YOLO26 / YOLOE** locally or on **Google Colab**, run real-time wireless/multi-camera detection, reconstruct 3D coronal brain slices from large TIFF stacks, or generate matched synthetic datasets from offline **Two-Mouse 3D**, **Rat NCAP 3D**, and **FlyBody** twins.

## Real-World Visual Showcase

### Multi-animal social tracking, 14 keypoints & live ethogram state

In a real resident-intruder home-cage trial (`mouse083_task1_annotator1`, 4,881 frames @ 30 FPS), Annolid tracks both whole-body polygons and 14 anatomical landmarks while synchronizing social behavior bouts (`investigation`, `mount`, `other`):

```{figure} ../images/showcase/mouse083_tracking_demo.gif
---
name: intro-mouse083-gif
alt: Animated multi-animal tracking demo showing resident and intruder polygons, 14 keypoints, trails, and live behavior overlay
width: 92%
---
Multi-animal instance masks, 7-keypoint skeletons per mouse, trajectory trails, and live behavior overlays on home-cage video. See the [full mouse083 walkthrough](../tutorials/mouse083_resident_intruder_showcase.md).
```

### Raw social interaction vs. tracked instance masks

:::::{container} ann-pair

:::{figure} ../images/interaction_raw.gif
:alt: Raw social interaction recording before Annolid tracking
**Before:** Raw multi-animal social interaction recording.
:::

:::{figure} ../images/interaction_analyzed.gif
:alt: Annolid tracked instance masks overlaid on social interaction video
**After:** Tracked per-individual masks ready for proximity and bout quantification.
:::

:::::

### Diverse species, arenas, and research paradigms

:::::{container} ann-gallery

::::{container} ann-card
![Multiple prairie vole tracking in a home cage](../images/mutiple_animal_tracking.png)

:::{container} ann-card-body
<div class="ann-card-title">Pair-Bonding &amp; Social Voles</div>

Whole-body instance tracking through close huddles and partial body occlusion in side-view home cages.
:::
::::

::::{container} ann-card
![Mouse object investigation tracking on a holeboard arena](../images/holeboard_mouse_tracking.png)

:::{container} ann-card-body
<div class="ann-card-title">Object Investigation &amp; Zones</div>

Track animals alongside arena stimuli and automatically associate proximity with user-defined zones.
:::
::::

::::{container} ann-card
![Multi-fly Drosophila arena tracked in Annolid GUI](../images/annolid_gui.png)

:::{container} ann-card-body
<div class="ann-card-title">Multi-Fly <em>Drosophila</em> Arenas</div>

Simultaneous identity-preserving tracking of eight flies in an open-field circular arena.
:::
::::

::::{container} ann-card
![Thermal urine spot and mouse tracking](../images/urine_tracking.png)

:::{container} ann-card-body
<div class="ann-card-title">Specialized Modalities (Thermal &amp; Microscopy)</div>

Segment non-standard targets such as thermal urine deposits, large TIFF brain sections, and multi-channel frames.
:::
::::

:::::

## Video Demonstrations

### Brief overview of Annolid

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/tVIE6vG9Gao" title="Introduction to Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Keypoint tracking & automated behavior recognition

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/op3A4_LuVj8" title="Animal tracking, keypoints, and automated behavior recognition" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Multiple animal tracking with partial occlusion

*Video courtesy of Caitlyn Finton and Alex Ophir.*

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/dZ-qsD8uu-U" title="Multi-animal tracking with occlusion in voles" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Freezing behavior & optical-flow motion scoring

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/qFABuhoGr_E" title="Freezing and dense optical flow motion scoring in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Large field-of-view multi-animal tracking

*Video courtesy of Santiago Forero and Alex Ophir.*

<div class="video_container">
  <iframe src="https://drive.google.com/file/d/1cYdmueC-CaMhScpcB2E-eL9mkGDFuVCs/preview" title="Large field-of-view multi-animal tracking" allowfullscreen></iframe>
</div>

## Explore More Examples

- Browse the full [Annolid YouTube tutorial playlist](https://www.youtube.com/playlist?list=PLYp4D9Y-8_dRXPOtfGu48W5ENtfKn-Owc).
- Need help with your own recordings or species? Reach out via [Get in touch](get_in_touch.md).
- Ready to see how all the pieces connect? Continue to [How Annolid Works (Technical Overview)](high_level_overview.md).
