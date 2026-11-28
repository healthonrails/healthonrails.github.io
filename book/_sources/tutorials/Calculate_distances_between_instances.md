# Inter-Instance Distances & Kinematics

Once you have tracked two or more animals — or an animal plus an arena stimulus such as a novel object or feeder — Annolid makes it easy to compute **frame-by-frame pairwise distances**, **close-contact bouts**, **speed**, and **path length** in pixels or calibrated centimeters.

```{figure} ../images/showcase/mouse083_ethogram_kinematics.png
---
name: dist-proximity-curve
alt: Resident-to-intruder centroid proximity curve aligned with shaded investigation and mounting bouts
width: 96%
---
Pairwise centroid distance between `resident` and `intruder` aligned against scored social bouts on `mouse083_task1_annotator1` (mean `280.5 px`, min `15.7 px`, `< 100 px` close-contact threshold).
```

## Prerequisites

You need a tracked video folder containing Annolid CSV outputs (`<video_stem>_tracking.csv` and `<video_stem>_tracked.csv`). If you only have per-frame JSON files so far, generate the CSVs in the GUI via **`File → Save CSV`** or via:

```bash
python -m annolid.annotation.labelme2csv --json_folder /path/to/video_results_folder
```

## Method 1 (Recommended): One-Command CLI (`annolid-run kinematics`)

Compute pairwise inter-animal distances, close-contact percentages, speed, straightness/tortuosity, and freezing bouts in one command — with optional real-world calibration:

```bash
# Uncalibrated pixel units
annolid-run kinematics mouse083_tracked.csv --fps 30 --output-dir ./kinematics_out

# Calibrated physical units (cm and cm/s) using scalar scale
annolid-run kinematics mouse083_tracked.csv \
  --fps 30 \
  --px-per-cm 12.5 \
  --output-dir ./kinematics_cm \
  --events-csv kinematics_bouts.csv

# Calibrated using 4-corner planar perspective homography (angled cameras)
annolid-run kinematics mouse083_tracked.csv \
  --fps 30 \
  --calibration arena_calibration.json \
  --output-dir ./kinematics_homography
```

## Method 2: Python API (`TrackingResultsAnalyzer`)

For custom Jupyter notebooks and exploratory pandas analysis, use Annolid's `TrackingResultsAnalyzer` helper class directly:

```python
from annolid.postprocessing.tracking_results_analyzer import TrackingResultsAnalyzer

analyzer = TrackingResultsAnalyzer(
    "/path/to/video.mp4",
    zone_file=None,  # optional: pass a *_zones.json file for zone metrics too
    fps=30,          # optional: auto-detected from video metadata when omitted
)
analyzer.merge_and_calculate_distance()
analyzer.distances_df.to_csv("inter_instance_distances.csv", index=False)
print(analyzer.distances_df.head())
```

The exported CSV contains `frame_number`, `instance_name_1`, `instance_name_2`, and `distance` (in pixels).

```{tip}
**Converting pixels to millimeters or centimeters:** Measure a known arena edge (for example a `40 cm` box wall spanning `500 px` → `12.5 px/cm`), then divide pixel distances by `12.5` — or pass `--px-per-cm 12.5` (or `--calibration arena_cal.json`) directly to `annolid-run kinematics` and `annolid-run report`.
```

Next: put Track QC, kinematics, zones, ethograms, IRR, and cohort stats together in [Track QC, Statistics & HTML5 Reports](Reporting_and_track_qc.md).
