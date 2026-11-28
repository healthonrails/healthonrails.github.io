# Spatial Zones & Place Preference

Spatial zone analysis measures **how long**, **how often**, and **how quickly** each tracked animal visits user-defined regions of an arena — such as open-field center vs. periphery, elevated-plus-maze arms, conditioned place-preference chambers, or three-chamber social zones.

```{figure} ../images/showcase/mouse083_zone_analysis.png
---
name: zones-mouse083-example
alt: Three home-cage arena zones overlaid with tracked mouse centroids and computed zone occupancy bar chart
width: 96%
---
Example zone layout (`left_nest_zone`, `center_arena`, `right_port_zone`) scored on `mouse083_task1_annotator1` with `annolid-run zone-analysis`.
```

## Method 1 (Recommended): Zone Dock & `annolid-run zone-analysis`

Annolid's modern **Zones** workflow supports **polygons**, **rectangles**, and **2-point circles**, saves reusable `*_zones.json` files with explicit `semantic_type=zone` metadata, and includes one-click arena presets (such as `3×3 Chamber Layout` and `3×3 Social Door Layout`).

### Step 1: Draw & Save Reusable Zones in the GUI

1. Open your video in Annolid (`File → Open Video`) on a clear reference frame.
2. Open **`Video Tools → Zones`** (or draw polygons on Frame 0 and add `zone` in the label description / zone flag).
3. Name each region clearly (for example `left_nest_zone`, `center_arena`, `right_port_zone`).
4. Save the zone layout as `<session>_zones.json` so you can reuse the exact same chamber geometry across every trial recorded on that rig!

```{figure} ../images/place_preference_zone.png
---
name: zones-draw-first-frame
alt: Drawing zone polygons on the first frame of a video and tagging them with the zone keyword
width: 92%
---
Labeling arena zones on a clean reference frame in Annolid.
```

### Step 2: Score Occupancy & Latency (GUI or CLI)

- **In the GUI**: Open **`File → Place Preference`** (or **`Analysis → Analysis & Reporting Studio…`**), select your tracked video / CSV and zone file, and click **Analyze**.

:::::{container} ann-pair

:::{figure} ../images/place_preference_menu.png
:alt: Opening Place Preference from the Annolid File menu
Launch Place Preference from the menu bar.
:::

:::{figure} ../images/place_preference_dialog.png
:alt: Place Preference dialog selecting tracked video and zone parameters
Select your tracked video or CSV and click **Analyze**.
:::

:::::

- **From the CLI (`annolid-run zone-analysis`)**:

```bash
# Generic zone metrics (occupancy %, duration, entries, latency, mean/max visit dwell)
annolid-run zone-analysis mouse083_tracked.csv \
  --zone-file mouse083_zones.json \
  --fps 30 \
  --mode zone_metrics \
  --output-dir ./zone_out

# Open-field or assay summary + visit events CSV
annolid-run zone-analysis session.mp4 \
  --zone-file session_zones.json \
  --profile open_field \
  --mode assay_summary \
  --events-csv zone_visits.csv
```

```{tip}
**Three-chamber social assays:** Mark connecting tunnels with `zone_kind=connector_tube` (or `occupant_role=neutral`) so neutral transit time is reported separately from social-chamber preference. See the full [Zone Analysis Reference](https://annolid.com/portal/zone_analysis/) on the Docs Portal.
```

---

## Bonus Walkthrough: Importing SLEAP Predictions for Zone Analysis

Already tracked keypoints in **SLEAP** (`.slp`, `.pkg.slp`, or `.analysis.h5`) or **DeepLabCut** (`.csv` / `.h5`)? You can import them straight into Annolid, review/edit frames visually, overlay your zones, and export CSV or HTML5 reports!

<div class="video_container">
  <iframe src="https://www.youtube.com/embed/tvLHj-Nwu-Y" title="Converting and analyzing SLEAP keypoint predictions in Annolid" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

### GUI Steps (SLEAP → Annolid → Zones)

1. **Create your zone file**: Open the video, draw arena zones on Frame 0, and save your `*_zones.json`.
2. **Import SLEAP predictions**: Open **`Tools → SLEAP (.slp / .h5) Import & Export…`** (or **`File → Load SLEAP h5`**), select your `.slp`, `.pkg.slp`, or `.analysis.h5` file, and run conversion to Annolid LabelMe JSON.
3. **Inspect in Annolid**: Open the video in Annolid — converted keypoint overlays and skeleton bones load automatically so you can verify frames and fix any swaps.
4. **Export CSV & analyze**: Run **`File → Save CSV`** (or `annolid-run zone-analysis` directly on the converted folder) to quantify zone occupancy and visits.

### Fast CLI Equivalent

```bash
# Import SLEAP .analysis.h5 or .pkg.slp directly to Annolid LabelMe JSON
annolid-run import-pose predictions.analysis.h5 --video trial.mp4 -o ./sleap_labelme
```

For bidirectional **DeepLabCut**, **Lightning Pose**, **SLEAP**, and **SimBA** recipes, see [Model Training & Pose Interoperability](../content/model_training.md).
