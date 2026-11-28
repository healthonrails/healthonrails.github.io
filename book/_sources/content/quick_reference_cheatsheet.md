# Quick Reference: Shortcuts, Files & Recipes

Bookmark this page as a one-screen lab-bench cheat sheet for everyday Annolid sessions.

## Essential GUI Keyboard Shortcuts

| Shortcut | Action |
| --- | --- |
| `Ctrl+S` *(macOS `Cmd+S`)* | Save current frame annotations / flags |
| `Ctrl+Z` / `Ctrl+Shift+Z` | Undo / Redo shape edits |
| `D` / `A` *(or `→` / `←`)* | Next / Previous frame or image |
| `Ctrl+Left-Click` *(macOS `Cmd+Click`)* | Finish **AI-Polygon** and assign label |
| `Shift+Click` *(Keypoint mode)* | Place an **occluded** keypoint (`v=1`, dashed bone) |
| `Ctrl+Shift+E` | Open **Extract Frames** dialog (`kmeans` / `uniform`) |
| `Ctrl+Shift+K` | Toggle **Keypoint Sequencer** dock |
| `Ctrl+Shift+P` | Open **Pose Estimation Workbench** |
| `Ctrl+Shift+R` | Open **Analysis & Reporting Studio** |
| `Ctrl+Shift+V` | Open **Training Monitor & Visualization** |
| `Ctrl+Enter` *(in Annolid Bot)* | Send prompt to **Annolid Bot** |
| `Delete` | Delete selected polygon / keypoint |
| `Ctrl+0` / Scroll Wheel | Fit image to window / Zoom in & out |

## Annolid File Naming Conventions

When you open `trial_01.mp4`, Annolid organizes outputs cleanly right next to your recording:

```text
trial_01.mp4
trial_01/
  project.annolid.json            # Shared ethogram behavior catalog (+ optional pose_schema_path)
  pose_schema.json                # Skeleton keypoints, bone edges, symmetry pairs & flip_idx
  trial_01_000000000.json         # Manual seed / edited LabelMe JSON frame
  trial_01_annotations.ndjson     # Compact append-only AnnotationStore for predicted frames
trial_01_zones.json               # Reusable spatial arena zones (semantic_type=zone)
trial_01_tracking.csv             # All shape rows: RLE masks, boxes, centroids
trial_01_tracked.csv              # Clean per-instance trajectories, speed & zone columns
trial_01_events.csv               # Behavior bouts (Behavior, Event start/stop, Timestamp)
```

## Copy-Paste `annolid-run` Command Cookbook

```bash
# Environment & model discovery
annolid-run runtime status
annolid-run list-models
annolid-run dinov3-models --list

# Track QC + unified HTML5/SVG scientific report
annolid-run track-qc trial_01_tracked.csv --expected-instances 2 --fps 30 --review-csv qc.csv
annolid-run report trial_01_tracked.csv --events-csv trial_01_events.csv --zone-file trial_01_zones.json --fps 30 --output-dir ./report

# Spatial zones & calibrated kinematics
annolid-run zone-analysis trial_01_tracked.csv --zone-file trial_01_zones.json --fps 30 --mode zone_metrics --output-dir ./zones_out
annolid-run kinematics trial_01_tracked.csv --fps 30 --px-per-cm 12.5 --output-dir ./kinematics_out --events-csv freezing.csv

# Natural-language behavior search (ONNX EmbeddingGemma 2 — no PyTorch needed)
annolid-run behavior-search trial_01.mp4 --query "mouse grooming" --stride 5 --index-cache ./trial_eg2.npz --json

# Pose extraction, evaluation, filtering & DLC/SLEAP interop
annolid-run extract-frames trial_01.mp4 --algo kmeans --num-frames 50 -o ./frames_kmeans
annolid-run eval-pose ./gt_labelme ./pred_labelme --pose-schema ./pose_schema.json --output-dir ./pose_eval
annolid-run import-pose trialDLC_filtered.csv --video trial_01.mp4 --min-likelihood 0.5 -o ./trial_labelme
annolid-run export-pose ./trial_labelme --format sleap-slp --embed-images -o ./trial.pkg.slp

# Cloud GPU & 3D Sim-to-Real
annolid-run colab status
annolid-run sim2real sample --video trial_01.mp4 --project ./s2r_mouse --species mouse --task yolo_pose --pose-schema mouse13
```

## Annolid Bot Slash Commands

| Command | Action |
| --- | --- |
| `/track` | Guided Cutie / SAM3 tracking form or inline tracking command |
| `/qc <path>` | Run automated Track QC & gap report |
| `/stats <path> [px_per_cm=12.5]` | Compute kinematics & tracking telemetry summary |
| `/report <path> [px_per_cm=12.5]` | Generate unified HTML5 + inline SVG report |
| `/sim2real [project=...]` | Open Sim-to-Real Studio |

## Fast Troubleshooting Table

| Symptom | Likely Cause | Fix |
| --- | --- | --- |
| `qtpy.QtBindingsNotFoundError` | Missing GUI extra | `pip install "annolid[gui]"` |
| Video fails to open or scrub | Missing FFmpeg/codec | Install FFmpeg and re-encode to H.264 `.mp4` (`libx264`) |
| Slow Cutie / SAM3 tracking | 4K or high-res video | Downsample to `0.5` (~640–960 px wide) via `File → Downsample Videos` |
| DINOv3 download fails (401/403) | Gated Hugging Face repo | Accept license on HF and run `hf auth login` (or use `facebook/dinov2-base`) |
| Two animals swapped IDs mid-video | Heavy occlusion crossing | Run `annolid-run track-qc`, fix 1 anchor frame (or run `swap-pose` / Identity Governor), and resume |
| Large TIFF pans sluggishly | Uncached flat TIFF | Install `annolid[large_image]` and run `File → Optimize Large TIFF for Fast Viewing…` |
