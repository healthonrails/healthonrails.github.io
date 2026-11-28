# Labeling Instances, Keypoints & Zones

Annolid builds on a fast, LabelMe-compatible canvas enhanced with **AI-assisted polygons**, **anatomical keypoints**, **spatial zones**, and **behavior flags**. Everything saves to human-readable JSON so your labels remain portable forever.

## Effortless AI-Assisted Labeling (SAM AI-Polygons)

Instead of tracing 30 polygon vertices by hand, switch to **AI-Polygon** mode and click once or twice on your animal — Annolid's Segment Anything backend snaps a clean contour automatically:

```{figure} ../images/showcase/ai_polygon_sam_demo.gif
---
name: label-ai-polygon-gif
alt: Animated demonstration of clicking points on animals in Annolid to generate SAM AI polygons automatically
width: 92%
---
One-click **AI-Polygon** labeling using Segment Anything inside Annolid: click foreground points to include an object, right-click or use negative prompts to exclude background, and press `Ctrl+Click` to finish and name the label.
```

## What Can You Label?

Because Annolid uses flexible instance shapes plus optional group IDs and metadata, you can annotate:

- **Whole-body animals** (`resident`, `intruder`, `mouse_1`, `mouse_2`, `fly_0`) — polygons or masks
- **Anatomical keypoints** (`nose`, `left_ear`, `right_ear`, `neck`, `left_hip`, `right_hip`, `tail_base`) — linked to an animal via `group_id`
- **Arena objects & landmarks** (`feeder`, `teaball`, `novel_object`, `nest`) — polygons or rectangles
- **Spatial zones** (`left_nest_zone`, `center_arena`, `right_port_zone`) — polygons, rectangles, or circles marked as zones
- **Behavior events** (`investigation`, `mount`, `grooming`, `rearing`, `freezing`) — frame flags or timeline intervals

```{figure} ../images/showcase/mouse083_gui_workspace.png
---
name: label-modern-workspace
alt: Modern Annolid GUI showing resident and intruder polygons, 14 keypoints, Flags dock, and Label Instances dock
width: 96%
---
The Annolid annotation workspace combining whole-body polygons, anatomical keypoints, the active behavior badge (`• investigation`), and synchronized right-hand docks.
```

## Step-by-Step: Label Your First Seed Frame

1. **Open your video** (`File → Open Video`) — or click **`Open Dir`** if you extracted images beforehand.
2. **Navigate to a clean seed frame** where all animals and objects of interest are clearly separated and unoccluded.
3. **Create a shape** using the toolbar or right-click canvas menu:
   - **`Create AI-Polygon`** *(fastest)*: click inside the animal; hold **`Ctrl` (macOS `Cmd`) + Left-Click** to finish the polygon and name it.
   - **`Create Polygons`**: click around the outline manually and close the loop on the first vertex.
   - **`Create Point`** (right-click → `Create Point` or Keypoint Sequencer): place named body-part keypoints.
   - **`Create Rectangle` / `Create Circle` / `Create Line`**: draw boxes, circular zones, or calibration lines.
4. **Edit or refine anytime**: click **`Edit Polygons`** to drag vertices, press `Delete` to remove a selected shape, or **`Ctrl+Z`** to undo.
5. **Save your seed frame** with **`Ctrl+S`** (`Cmd+S` on macOS). Annolid saves `<video_stem>/<video_stem>_#########.json` (plus a PNG snapshot for reference frames).

```{figure} ../images/labelling_0.png
---
name: label-classic-zones
alt: Example of labeled animal instances and arena zones inside Annolid
width: 85%
---
Cleanly separated instance and zone polygons make downstream tracking and place-preference analysis straightforward.
```

```{tip}
**Keyboard shortcuts that save hours:**
- `Ctrl+S` (`Cmd+S`): Save current frame
- `Ctrl+Z` / `Ctrl+Shift+Z`: Undo / Redo polygon edits
- `D` / `A` (or Left/Right arrows): Next / Previous frame
- `Scroll wheel` / `Ctrl+0`: Zoom in/out and fit to window
```

## Naming Rule: Individual Tracking vs. Class Generalization

How you name your labels tells Annolid whether to preserve individual identities or generalize across animals:

| Your Goal | How to Name Labels | Example |
| --- | --- | --- |
| **Track specific individuals** across frames (multi-animal identity) | Give each animal its own unique label | `resident`, `intruder` or `vole_1`, `vole_2` |
| **Train a general detector** that recognizes *any* animal of that type across new videos | Use the same shared class label for all animals of that class | `mouse`, `vole`, `fly` |
| **Combine body polygons + keypoints** | Group keypoints with their animal's `group_id` or prefix | `resident` + `resident_nose`, `resident_tail_base` |

```{warning}
If you manually edit a saved `labels.txt` file outside Annolid, keep the first two header lines (`__ignore__` and `_background_`) intact if they are present.
```

## How Many Frames Should You Label?

- **For Cutie, SAM3, INSID3, or DINOv3 Keypoints (training-free):** Start with **just 1 clean frame**! Only label extra correction frames later if an occlusion causes drift.
- **For custom YOLO11 / YOLO26 training:** Start with **20–50 diverse frames** (using the `Small Lab Dataset` preset), evaluate on a test clip, and expand toward **100–150 frames** only where errors remain.

```{figure} ../images/labelling_1.png
---
name: label-accuracy-curve
alt: Illustration of segmentation accuracy improving as more labeled frames are added
width: 72%
---
Even a small set of diverse seed frames goes a long way when paired with human-in-the-loop correction.
```

## Video Tutorials

### Labeling zones & saving labels in Annolid

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/pb8X4bqLRZ0" title="Labeling zones and saving labels in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Annotating instances step by step

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/zX8cUImRI_s" title="Annotating instances step by step in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### Multi-animal tracking & re-identification example

*Video courtesy of Lindsay Sailer and Alex Ophir.*

<div class="video_container">
  <iframe src="https://drive.google.com/file/d/1uw_0JO_rB6Adq7YEHrapzDdGEOPxsmhC/preview" title="Multi-animal re-identification example" allowfullscreen></iframe>
</div>

Next: see how [AI point prompts and text prompts work under the hood](labeling_instances_under_the_hood.md), or jump straight into [Tracking with Cutie](tracking_with_Cutie.md).
