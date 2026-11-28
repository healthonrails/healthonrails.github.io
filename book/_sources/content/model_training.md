# Model Training & Pose Interoperability

You do **not** always need to train a custom neural network to succeed with Annolid. For single trials or small pilot studies, labeling 1 frame and propagating with **[Cutie](tracking_with_Cutie.md)**, **[SAM3](../tutorials/SAM3_video_tracking.md)**, **[INSID3](../tutorials/INSID3_video_segmentation.md)**, or **[DINOv3 Keypoints](../tutorials/DINOv3_keypoint_tracking.md)** is often faster.

Train a custom model when you need:

- **high-throughput speed** across dozens or hundreds of cohort videos,
- **real-time camera inference** (for closed-loop or wireless camera setups),
- **generalization** across sessions, arenas, or species, or
- **reusable multi-animal pose estimation** with named anatomical skeletons.

## Recommended Path: Fine-Tune YOLO11 / YOLO26 / YOLOE

Annolid integrates Ultralytics **YOLO11**, **YOLO26**, and open-vocabulary **YOLOE** for detection, instance segmentation, and pose estimation — with guided presets for small lab datasets.

### Step 1: Prepare or Export Your Dataset

Annolid's **Training Wizard** and `annolid-run` accept any of these directly:

- a standard YOLO `data.yaml` (or folder containing `YOLO_dataset/data.yaml`),
- a **COCO** dataset folder (detection, polygon/RLE segmentation, or keypoints — auto-converted non-destructively), or
- **Annolid LabelMe JSON** frames exported via **`File → Convert Labelme to YOLO format`** or the CLI:

```bash
# Modern dataset index -> YOLO export
annolid-run collect-labels --input /path/to/labeled_frames --output dataset_index.jsonl
annolid-run index-to-yolo --index dataset_index.jsonl --output ./yolo_dataset

# Classic direct conversion helper
python -m annolid.main --labelme2yolo /path/to/labelme_json_folder --val_size 0.1 --test_size 0.1
```

### Step 2: Pick a Fine-Tuning Preset in the Training Wizard

Open **`AI & Models → Training Wizard…`**:

1. **Select Dataset**: Browse to your YOLO `data.yaml` or COCO folder. Annolid inspects class names, image counts, and task type (Detection / Segmentation / Pose) automatically.
2. **Choose Backend**: Select **YOLO (Ultralytics)** (or **DINO KPSEG** / **Keypoint R-CNN** for pose tasks).
3. **Configure Preset & Hardware**:

| Preset | Best For | Key Defaults |
| --- | --- | --- |
| **`Small Lab Dataset (Fine-tune)`** | ~20–150 labeled frames | 120 epochs, AdamW, `lr0=0.002`, `freeze=10`, cosine LR |
| **`Balanced (Recommended)`** | 150+ labeled frames | 100 epochs, 640 px, patience 50, cosine LR |
| **`Quick Smoke Test`** | Checking labels & class map | 30 epochs, batch 16 |
| **`High Accuracy (960px)`** | Small animals or fine body parts | 200 epochs, 960 px, AdamW |

4. **Launch locally or on Google Colab**: Run on NVIDIA CUDA, Apple Silicon MPS, or CPU — or click **Run on Google Colab…** to offload training to a cloud GPU.

### Step 3: Monitor Runs & Compare Experiments (`Ctrl+Shift+V`)

Open **`AI & Models → Training Monitor & Visualization…`** (`Ctrl+Shift+V`) to:

- watch live loss, mAP, PCK, and learning-rate curves with EMA smoothing,
- compare multiple checked runs side by side with a highlighted hyperparameter diff table,
- star favorite checkpoints, add lab notes/tags, and receive automated health diagnostics (`NaN`/spike/overfitting/plateau alerts), and
- export an offline **HTML5 + inline SVG** experiment report or open embedded **TensorBoard**.

When training completes, select your trained `best.pt` directly from the **AI Model** selector (or **Browse Custom YOLO…**).

## Bidirectional DeepLabCut, SLEAP & COCO Interoperability

Already have labeled data or predictions from **DeepLabCut**, **Lightning Pose**, **SLEAP**, **SimBA**, or **COCO**? Annolid imports and exports all of them cleanly — both from **`Tools → DeepLabCut / Lightning Pose Import & Export…`**, **`Tools → SLEAP (.slp / .h5) Import & Export…`**, and the CLI:

```bash
# Import DeepLabCut / Lightning Pose CSV or H5 into Annolid LabelMe JSON
annolid-run import-pose trialDLC_dlcrnet_filtered.csv --video trial.mp4 --min-likelihood 0.5 -o ./trial_labelme

# Import a SLEAP project (.slp / .pkg.slp) or analysis HDF5 (.analysis.h5)
annolid-run import-pose predictions.analysis.h5 --video trial.mp4 -o ./sleap_labelme

# Export Annolid annotations or tracking to DeepLabCut, SimBA, or SLEAP
annolid-run export-pose ./trial_labelme --format deeplabcut-csv --scorer my_lab -o ./trial_dlc.csv
annolid-run export-pose ./trial_tracking.csv --format sleap-h5 --video ./trial.mp4 -o ./trial.analysis.h5
```

## Optional: Legacy Mask R-CNN via Detectron2

If your lab maintains an existing Detectron2 Mask R-CNN pipeline:

- Prefer [Annolid on Google Colab](Annolid_on_Google_Colab.md) for a ready-to-run GPU notebook.
- Export LabelMe frames to COCO format via **`File → COCO format`**.

```{tip}
**Zero labeled frames yet?** You can also bootstrap a working mouse, rat, or fly segmentation/pose model from raw videos using [Sim-to-Real Studio](../tutorials/Simulation_3d_digital_twins.md). For complete YOLO CLI flags and pose workflows, see the [YOLO Workflow](https://annolid.com/portal/yolo_workflow/) and [Pose Interoperability](https://annolid.com/portal/pose_interoperability/) guides on the Docs Portal.
```
