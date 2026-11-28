# Polygon-Feature TCN Behavior Classification

Want automated frame-by-frame behavior scoring (`still`, `walk`, `groom`, `rearing`, `investigation`) trained directly on your tracked **polygons** or **DeepLabCut/SLEAP pose markers**? Annolid includes a DAART-style **Temporal Convolutional Network (TCN)** pipeline designed around strict scientific hygiene (leakage-free session splitting, masked padding steps, and gap-aware temporal smoothing).

```{figure} ../images/diagrams/tcn_behavior_pipeline.png
---
name: tcn-pipeline-diagram
alt: Four-stage leakage-safe TCN behavior classification pipeline from polygon or marker CSVs through group-split and dilated TCN to gap-aware smoothed ethograms
width: 100%
---
Annolid's TCN behavior classifier turns tracked geometry and kinematics into smooth, session-validated ethograms.
```

## Two Ways to Run TCN Training

::::{tab-set}

:::{tab-item} Desktop GUI (Polygon Classifier Workbench)
Starting from Annolid polygon tracking? You do **not** need to write YAML configs by hand:

1. Open **`Tools → Polygon Classifier Workbench`**.
2. Generate or select your tracked polygon feature CSV + labeled behavior events.
3. In the **Training** tab, choose **`TCN`** as the model type.
4. Click **Train** — Annolid builds dense per-video TCN inputs automatically, splits train/validation cleanly by `source_group` before any class balancing, and saves `polygon_tcn_classifier_best.pt`.
5. Switch to the **Inference** tab to score new unseen videos and export timeline-ready behavior CSVs!
:::

:::{tab-item} CLI (`annolid-run train/predict tcn_behavior`)
Create a clean YAML config (`tcn_behavior.yaml`) listing your train and held-out test sessions:

```yaml
labels:
  - background
  - still
  - walk
  - groom

sessions:
  - id: session_001
    features: /path/to/session_001_labeled.csv
    labels: /path/to/session_001_labels.csv
    split: train
  - id: session_002
    features: /path/to/session_002_labeled.csv
    labels: /path/to/session_002_labels.csv
    split: test

feature:
  input_type: features   # use "markers" for DLC marker CSVs
  add_velocity: true
  zscore: true

model:
  hidden_dim: 32
  num_blocks: 2
  kernel_size: 9
  dropout: 0.1

training:
  epochs: 500
  batch_size: 8
  sequence_length: 1000
  learning_rate: 0.0001
  device: auto
```

Train and predict from the terminal:

```bash
# 1. Train (writes best_model.pt and metrics.json)
annolid-run train tcn_behavior \
  --config /path/to/tcn_behavior.yaml \
  --output-dir /path/to/tcn_run

# 2. Predict with temporal probability smoothing (odd window size)
annolid-run predict tcn_behavior \
  --config /path/to/tcn_behavior.yaml \
  --checkpoint-path /path/to/tcn_run/best_model.pt \
  --output-csv /path/to/predictions.csv \
  --metrics-json /path/to/test_metrics.json \
  --smoothing-window 51
```
:::

::::

## Scientific Guardrails Built Into Annolid's TCN

- **Zero train/val data leakage**: Sessions are partitioned by `source_group` *before* oversampling so consecutive frames from the same bout never leak between train and validation.
- **Sparse labeling supported**: Unlabeled `background` (first label in `labels:`) and padded sequence tails (`-100`) are ignored in the cross-entropy loss.
- **Gap-aware smoothing**: Temporal probability smoothing (`--smoothing-window`) splits across non-contiguous frame gaps instead of blurring across missing intervals. Choose your window size on a validation split, never by tuning on the final test set!

```{tip}
Want step-by-step advice on collecting balanced polygon training videos and setting up held-out validation splits? See [Polygon TCN Video Collection](https://annolid.com/portal/tutorials/polygon_tcn_video_collection/) and [TCN Behavior Classification](https://annolid.com/portal/tutorials/tcn_behavior_pipeline/) on the Docs Portal.
```
