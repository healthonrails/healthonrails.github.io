# Featured Walkthrough: Resident-Intruder Social Assay (`mouse083`)

This end-to-end walkthrough follows one real two-mouse home-cage recording (**`mouse083_task1_annotator1.mp4`**: `1024 × 570`, `30 FPS`, `4,881 frames`, `162.7 s`) from first GUI click to a publication-ready HTML5 + SVG report.

<div class="ann-stats">
  <div class="ann-stat">
    <strong>4,881 frames</strong>
    <span>162.7 s @ 30 FPS (1024 × 570)</span>
  </div>
  <div class="ann-stat">
    <strong>2 masks + 14 keypoints</strong>
    <span>resident &amp; intruder · 7 landmarks each</span>
  </div>
  <div class="ann-stat">
    <strong>39.1 s / 19.9 s</strong>
    <span>investigation (25 bouts) · mount (7 bouts)</span>
  </div>
  <div class="ann-stat">
    <strong>5-frame QC alert</strong>
    <span>intruder occlusion flagged at 3361–3366</span>
  </div>
</div>

<div class="ann-cta-row">
  <a class="ann-cta ann-cta--primary" href="https://annolid.com/portal/assets/reports/mouse083_report.html" target="_blank" rel="noopener">Open Live Interactive HTML5/SVG Report →</a>
  <a class="ann-cta" href="Reporting_and_track_qc.html">Track QC &amp; Reporting Guide</a>
  <a class="ann-cta" href="Simulation_3d_digital_twins.html">Matching 3D Digital Twin</a>
</div>

## Animated Multi-Animal Tracking & Behavior Preview

```{figure} ../images/showcase/mouse083_tracking_demo.gif
---
name: mouse083-tracking-demo
alt: Animated resident-intruder tracking demo showing cyan resident and orange intruder polygons, 14 keypoints, trails, and live behavior banner
width: 92%
---
Tethered black resident (`resident`, cyan contour + 7 keypoints) interacting with a white intruder (`intruder`, amber contour + 7 keypoints) on textured aspen bedding near a right-wall feeder port.
```

## 1. Transparent Project Files on Disk

Every stage stays human-readable and versionable in plain JSON and CSV files:

```text
mouse083_task1_annotator1.mp4                  # Source 30 FPS video (1024 × 570, 4,881 frames)
mouse083_task1_annotator1/
  project.annolid.json                         # Shared ethogram schema (other, investigation, mount)
  mouse083_task1_annotator1_000000000.json     # Per-frame LabelMe JSON (2 polygons + 14 keypoints + flags)
  ...
  mouse083_task1_annotator1_000004880.json
mouse083_task1_annotator1_tracking.csv         # 78,091 rows: RLE masks, boxes, centroids for all 16 shapes
mouse083_task1_annotator1_tracked.csv          # 9,757 rows: per-animal centroids, motion index, timestamps
```

Each annotated frame contains:
- **2 whole-animal polygons**: `resident` and `intruder`
- **14 anatomical keypoints** (7 per mouse, linked by `group_id`): `nose`, `left_ear`, `right_ear`, `neck`, `left_hip`, `right_hip`, `tail_base`
- **Frame-level ethogram flags**: `other`, `investigation`, or `mount`

## 2. Labeling & Review Inside the Desktop GUI

```{figure} ../images/showcase/mouse083_gui_workspace.png
---
name: mouse083-gui-workspace
alt: Annolid desktop GUI open on mouse083_task1_annotator1 with polygons, keypoints, investigation overlay pill, Flags dock, and Label Instances dock
width: 96%
---
The Annolid desktop workspace synchronizes polygons, keypoints, viewport-pinned behavior badges (`• investigation`), **Flags**, **Label Instances**, **Video List**, and **Behavior Controls**.
```

To run this workflow on your own recording:

1. Open your video directly (`File → Open Video`) — no frame extraction required.
2. Seed `Frame 0000` with whole-body polygons (**Create AI-Polygon**) and anatomical keypoints.
3. Track polygons forward with **[Cutie](../content/tracking_with_Cutie.md)**, **[SAM3](SAM3_video_tracking.md)**, or **YOLO**, and track keypoints with **[DINOv3 Keypoint Tracking](DINOv3_keypoint_tracking.md)**.
4. Score behaviors (`investigation`, `mount`, `other`) via **Flags**, the **Timeline** needle, or **Annolid Bot** 1-second segment labeling.

## 3. Tracking Through Close Contact & Catching Occlusions With Track QC

Real social trials alternate between clear separation and heavy overlap where one mouse temporarily hides the other.

```{figure} ../images/showcase/mouse083_behavior_storyboard.png
---
name: mouse083-storyboard
alt: Four-panel storyboard of mouse083 showing Seed Frame, Social Investigation, Mounting Bout, and Track QC Occlusion Alert
width: 100%
---
**Four key moments across the trial:** (A) clean seed frame (`494 px` separation), (B) nose-to-body `investigation` (`143 px`), (C) high-overlap `mount` (`114 px`), and (D) a 5-frame occlusion dropout automatically caught by **Track QC** at frames `3361–3366`.
```

Run automated **Track QC** to rank the highest-risk frames for targeted human review instead of guessing where errors occurred:

```bash
annolid-run track-qc mouse083_task1_annotator1_tracked.csv \
  --expected-instances 2 \
  --fps 30 \
  --review-csv mouse083_review_queue.csv \
  --out mouse083_track_qc.json
```

Double-clicking row `#1` in **Analysis → Analysis & Reporting Studio… → Track QC & Gaps** jumps your canvas straight to frame `3361` so you can repair one anchor frame and re-propagate cleanly.

## 4. Ethogram Timeline, Social Proximity & Arena Trajectories

```{figure} ../images/showcase/mouse083_ethogram_kinematics.png
---
name: mouse083-ethogram-kinematics
alt: Ethogram timeline raster, inter-animal centroid proximity curve, thigmotaxis trajectories, and behavior time budget for mouse083
width: 100%
---
Scored ethogram bouts align tightly with sharp drops in inter-animal distance (`< 100 px` close-contact threshold), while full-session trajectories reveal clear wall-following thigmotaxis.
```

| Metric | `resident` | `intruder` |
| --- | --- | --- |
| Observed Frames (Coverage) | 4,881 / 4,881 (`100.0%`) | 4,876 / 4,881 (`99.9%`) |
| Path Distance | `27,173.4 px` | `20,957.8 px` |
| Mean Speed | `167.06 px/s` | `128.78 px/s` |
| Freezing % (Bouts) | `3.5%` (`7` bouts) | `4.0%` (`9` bouts) |
| Inter-Animal Distance | Mean `280.5 px` · Min `15.7 px` | Close contact (`< 100 px`): `5.7%` |

Behavior time budget across the `162.7 s` recording:

| Behavior | Bouts | Total Duration | Mean Bout | Median Bout | % of Session |
| --- | --- | --- | --- | --- | --- |
| `other` | 24 | `103.70 s` | `4.32 s` | `3.65 s` | `63.7%` |
| `investigation` | 25 | `39.07 s` | `1.56 s` | `0.63 s` | `24.0%` |
| `mount` | 7 | `19.90 s` | `2.84 s` | `2.57 s` | `12.2%` |

## 5. Spatial Zone & Place-Preference Scoring

Define reusable arena zones once in **Video Tools → Zones** (`mouse083_zones.json`) and score occupancy and entries in one command:

```bash
annolid-run zone-analysis mouse083_task1_annotator1_tracked.csv \
  --zone-file mouse083_zones.json \
  --fps 30 \
  --mode zone_metrics \
  --output-dir ./mouse083_zone_out
```

```{figure} ../images/showcase/mouse083_zone_analysis.png
---
name: mouse083-zone-analysis
alt: Three home-cage zones overlaid on mouse083 alongside bar chart of occupancy durations and entry counts
width: 100%
---
Spatial zone polygons (`left_nest_zone`, `center_arena`, `right_port_zone`) overlaid with tracked centroids and computed occupancy durations and entry counts.
```

Both animals spend over **78%** of the trial in the two end zones (`left_nest_zone` and `right_port_zone`) and transit quickly across `center_arena` (`1.10–1.59 s` mean visit).

## 6. One-Command Unified HTML5 + Inline SVG Report

Combine Track QC, kinematics, spatial zones, body-part contact ethograms, and behavior time budgets into one shareable, offline HTML5 report:

```bash
annolid-run report mouse083_task1_annotator1_tracked.csv \
  --events-csv mouse083_events.csv \
  --zone-file mouse083_zones.json \
  --schema mouse083_task1_annotator1/project.annolid.json \
  --fps 30 \
  --title "mouse083_task1_annotator1 — Resident-Intruder Social Assay" \
  --output-dir ./mouse083_report
```

```{figure} ../images/showcase/mouse083_report_preview.png
---
name: mouse083-report-preview
alt: Preview of the self-contained HTML5 and inline SVG report generated by annolid-run report
width: 96%
---
Preview of the generated self-contained HTML5/SVG report ([open the live interactive report](https://annolid.com/portal/assets/reports/mouse083_report.html)).
```

## 7. Pair Real Recordings With 3D Digital Twins

Want synthetic ground-truth pose, body-part masks, or controlled occlusion tests modeled on the same black C57BL/6 + white BALB/c paradigm? Continue to [3D Digital Animal Twins & Sim-to-Real Studio](Simulation_3d_digital_twins.md).
