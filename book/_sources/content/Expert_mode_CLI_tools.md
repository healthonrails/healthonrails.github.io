# Power-User CLI (`annolid` & `annolid-run`)

Most researchers start in the desktop GUI (`annolid`). Once your pipeline works on one video, Annolid's composable command-line interface (**`annolid-run`**) lets you automate entire lab cohorts, run headless jobs on remote Linux servers or Google Colab, and plug Annolid cleanly into scripts.

## 1. Launching the GUI (`annolid`)

The `annolid` entrypoint supports handy launch flags for pre-loading project labels and behavior flags:

```bash
# Check installed version
annolid --version

# Launch with custom instance labels & behavior flags pre-populated
annolid --labels "resident,intruder" --flags "investigation,mount,grooming"

# Enable automatic saving on frame change
annolid --autosave

# See all GUI flags
annolid --help
```

## 2. Composable Pipeline CLI (`annolid-run`)

Run `annolid-run --help` or `annolid-run list-models` to discover every available command and model plugin in your environment.

### Model Discovery & Runtime Management

```bash
annolid-run list-models
annolid-run help train yolo
annolid-run help predict yolo_labelme
annolid-run runtime status
annolid-run runtime install tracking sam3
annolid-run dinov3-models --list
```

### Track QC, Kinematics, Zones & One-Command HTML5 Reports

```bash
# 1. Automated Track QC & prioritized manual review queue
annolid-run track-qc mouse083_tracked.csv \
  --expected-instances 2 \
  --fps 30 \
  --review-csv review_queue.csv \
  --out track_qc.json

# 2. Calibrated kinematics, freezing bouts & pairwise distance
annolid-run kinematics mouse083_tracked.csv \
  --fps 30 \
  --px-per-cm 12.5 \
  --output-dir ./kinematics_out

# 3. Spatial zone & place-preference metrics
annolid-run zone-analysis mouse083_tracked.csv \
  --zone-file mouse083_zones.json \
  --fps 30 \
  --mode zone_metrics \
  --output-dir ./zone_out

# 4. Unified self-contained HTML5 + inline SVG + Markdown + JSON report
annolid-run report mouse083_tracked.csv \
  --events-csv mouse083_events.csv \
  --zone-file mouse083_zones.json \
  --fps 30 \
  --title "Resident-Intruder Assay" \
  --output-dir ./session_report
```

### Behavior Ethograms, BORIS, IRR & Cohort Statistics

```bash
# Behavior time budget (60s bins + SVG ethogram + transition graph)
annolid-run time-budget session_events.csv \
  --schema project.annolid.json \
  --bin-size 60 \
  --ethogram-svg ethogram.svg \
  --transitions-svg transitions.svg \
  -o time_budget.csv

# Import/export BORIS projects
annolid-run boris-import study.boris --output-dir ./annolid_from_boris
annolid-run boris-export session_events.csv --schema project.annolid.json --format boris --output session.boris

# Inter-rater reliability (Cohen's kappa, Fleiss' kappa, Krippendorff's alpha)
annolid-run behavior-irr rater1.csv rater2.csv --bin-seconds 0.1 --out irr_report.json

# Cohort-level statistical comparisons with Benjamini-Hochberg FDR
annolid-run behavior-cohort ./cohort_manifest.json --unit recording --out cohort_report.json
```

### Pose Interoperability (DeepLabCut, SLEAP, Lightning Pose, SimBA)

```bash
# Import DLC or SLEAP into Annolid LabelMe JSON
annolid-run import-pose trialDLC_filtered.csv --video trial.mp4 --min-likelihood 0.5 -o ./trial_labelme
annolid-run import-pose predictions.analysis.h5 --video trial.mp4 -o ./sleap_labelme

# Export Annolid annotations or tracking CSV to DLC or SLEAP
annolid-run export-pose ./trial_labelme --format deeplabcut-csv --scorer lab1 -o ./trial_dlc.csv
annolid-run export-pose ./trial_tracking.csv --format sleap-h5 --video ./trial.mp4 -o ./trial.analysis.h5
```

### Cloud GPU (`colab`) & 3D Sim-to-Real (`sim2real`)

```bash
# Google Colab training & inference
annolid-run colab status
annolid-run colab train yolo --data ./yolo_dataset/data.yaml --weights yolo11s-seg.pt --gpu T4

# Sim-to-Real 3D synthetic bootstrap & iteration
annolid-run sim2real sample --video trial_01.mp4 --project ./s2r_mouse --species mouse --task yolo_pose --pose-schema mouse13
annolid-run sim2real iterate --project ./s2r_mouse --model yolo --train-backend colab --gpu T4 --epochs 30
```

## 3. Classic Python Module Helpers (`python -m`)

Existing scripts using Annolid's classic module entrypoints continue to work seamlessly:

```bash
# Convert LabelMe JSON folder -> tracking CSV
python -m annolid.annotation.labelme2csv --json_folder /path/to/video_results_folder

# Convert LabelMe JSON folder -> YOLO dataset
python -m annolid.main --labelme2yolo /path/to/labelme_json_folder --val_size 0.1 --test_size 0.1

# Compute behavior time budget CSV
python -m annolid.behavior.time_budget /path/to/exported_events.csv -o time_budget.csv --bin-size 60
```

```{tip}
For complete CLI schemas and agent-safe execution patterns, see [Annolid Agent and `annolid-run`](https://annolid.com/portal/agent_annolid_run/) and [Reporting & Statistics Reference](https://annolid.com/portal/reporting_and_statistics/) on the Docs Portal.
```
