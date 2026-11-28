# Pose Estimation & DeepLabCut / SLEAP Interoperability

Annolid includes a full **Pose Estimation Workbench** (`Ctrl+Shift+P`) with DeepLabCut and SLEAP feature parity — covering species skeleton presets, *k*-means diverse frame extraction, rapid sequential keypoint labeling, model evaluation (RMSE, PCK, OKS/mAP), active-learning outlier mining, trajectory filtering, identity-swap repair, calibrated pose kinematics, and bidirectional format exchange.

```{figure} ../images/diagrams/pose_interop_ecosystem.png
---
name: pose-interop-diagram
alt: Diagram of Annolid Pose Hub exchanging skeletons bidirectionally with DeepLabCut, Lightning Pose, SLEAP, COCO, and SimBA while powering eval-pose, filtering, kinematics, and labeled videos
width: 100%
---
Annolid's Pose Hub lets you move skeletons cleanly between DeepLabCut, Lightning Pose, SLEAP, COCO, SimBA, and Annolid's interactive GUI.
```

## 1. Define a Skeleton (`PoseSchema`)

Open **Project Wizard → Pose Schema** or **Settings → Pose & Keypoint Manager** and pick a built-in species preset:

- **Rodents**: `Mouse (5 keypoints)`, `Mouse CalMS21 / MARS (7 keypoints)`, `Mouse (9 keypoints)`, `Mouse (11 keypoints)`, `Mouse MaBE2022 (12 keypoints)`, `Rat (8 keypoints)`
- **Insects & Fish**: `Fly (5 keypoints)`, `Fly Full-Body (12 keypoints)`, `Fish (5 keypoints)`, `Zebrafish Spine (5 keypoints)`
- **Human**: `Human COCO (17 keypoints)`

Skeletons save to `pose_schema.json` (keypoint order, anatomical bone edges, left/right `symmetry_pairs`, and `flip_idx`) and auto-load whenever you open a matching video or annotation folder.

## 2. Extract Diverse Training Frames (`kmeans`)

Sample visually diverse postures rather than repetitive resting frames using deterministic *k*-means++ clustering:

```bash
annolid-run extract-frames trial.mp4 --algo kmeans --num-frames 50 -o ./frames_kmeans
```

Or run **Video Tools → Extract frames** (`Ctrl+Shift+E`) in the GUI and select **`kmeans`**.

## 3. Fast Keypoint Labeling & Proofreading in the GUI

Open the **Keypoint Sequencer** dock (`Ctrl+Shift+K` or **View → Docks → Keypoint Sequencer**):

- Click landmarks in locked sequence; use **Skip (Absent)** for out-of-frame points and **Auto-advance to next instance** in multi-animal videos.
- **Occluded keypoints (`v=1`)**: Hold **`Shift+Click`** to mark an occluded landmark (rendered with dashed bones and hollow circles).
- **Whole-skeleton edits**: Right-click any keypoint to **Select Whole Pose Instance**, drag the entire skeleton at once, or rotate (`±15°`) / scale (`±10%`) around its centroid.
- **Live canvas coloring**: Inside **Analysis → Pose Estimation Workbench…** (`Ctrl+Shift+P`), toggle coloring **By Instance**, **By Bodypart (DLC)**, or **By Confidence**, and adjust the live **p-cutoff** slider.

:::::{container} ann-pair

:::{figure} ../images/showcase/mouse_keypoints.png
:alt: Anatomical mouse keypoint landmarks in Annolid
Clean per-animal anatomical landmarks with `pose_schema.json` bone edges.
:::

:::{figure} ../images/showcase/mouse083_tracking_hero.png
:alt: Multi-animal polygon and 14-keypoint skeleton overlay on mouse083
High-contrast per-instance skeleton rendering across close dyadic interactions.
:::

:::::

## 4. Evaluate, Refine Outliers, Filter & Repair Swaps

```bash
# 1. DeepLabCut RMSE/MAE + SLEAP p50/p95 + PCK + COCO OKS HTML5 report
annolid-run eval-pose ./gt_labelme ./pred_labelme \
  --pose-schema ./pose_schema.json \
  --pcutoff 0.6 \
  --output-dir ./pose_eval_report

# 2. Active-learning outlier mining (extracts worst frames ready to drag & fix in GUI)
annolid-run extract-outliers ./pred_labelme \
  --video trial.mp4 \
  --pose-schema ./pose_schema.json \
  --num-frames 20 \
  --min-frame-gap 15 \
  -o ./refinement_batch

# 3. Offline filtering + bounded gap interpolation + bone-length sanity bounds
annolid-run filter-pose ./pred_labelme \
  --pose-schema ./pose_schema.json \
  --min-confidence 0.5 \
  --max-jump-px 45 \
  --enforce-bone-bounds \
  --interpolate linear --max-gap 5 \
  --method savgol --window 5 \
  -o ./pred_filtered

# 4. Swap two mislabeled animals from frame 420 forward (updates polygons + keypoints together)
annolid-run swap-pose ./pred_labelme \
  --start-frame 420 --instance-a mouse_1 --instance-b mouse_2
```

## 5. Bidirectional DeepLabCut, SLEAP & COCO Conversion

Use **Tools → DeepLabCut / Lightning Pose Import & Export…**, **Tools → SLEAP (.slp / .h5) Import & Export…**, or the CLI:

| Ecosystem | Import (`import-pose`) | Export (`export-pose`) |
| --- | --- | --- |
| **DeepLabCut / Lightning Pose** | 3- & 4-row CSV/H5 + `labeled-data/` + `config.yaml` | `--format deeplabcut-csv`, `deeplabcut-h5`, `deeplabcut-project` |
| **SLEAP** | `.slp`, `.pkg.slp`, `.analysis.h5` | `--format sleap-h5`, `sleap-slp` (`--embed-images` for `.pkg.slp`) |
| **SimBA / B-SOiD / VAME / `movement`** | Standard DLC CSV or SLEAP `.analysis.h5` | `--format simba`, `deeplabcut-csv`, or `sleap-h5` |
| **COCO Keypoints** | COCO JSON + skeleton auto-schema | Canonical `PoseSchema` COCO JSON + `coco2deeplabcut` |

```bash
# Import DLC or SLEAP into Annolid
annolid-run import-pose trialDLC_filtered.csv --video trial.mp4 --min-likelihood 0.5 -o ./trial_labelme
annolid-run import-pose labels.pkg.slp -o ./sleap_labelme --write-index

# Export Annolid to DLC, SimBA, or self-contained SLEAP .pkg.slp
annolid-run export-pose ./trial_labelme --format deeplabcut-csv --scorer my_lab -o ./trial_dlc.csv
annolid-run export-pose ./trial_labelme --format sleap-slp --embed-images -o ./trial.pkg.slp
```

```{tip}
For calibrated joint angles, egocentric pose coordinates (`annolid-run pose-kinematics`), and labeled skeleton video export, see the [Pose Estimation Workflow](https://annolid.com/portal/pose_estimation_workflow/) and [Pose Interoperability](https://annolid.com/portal/pose_interoperability/) guides on the Docs Portal.
```
