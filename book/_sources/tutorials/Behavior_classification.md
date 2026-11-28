# Behavior Scoring, Timelines & Ethograms

Annolid supports the full spectrum of behavioral ethogram workflows — from rapid manual keyboard/timeline scoring and **BORIS** interoperability to **Annolid Bot** 1-second video-language labeling and supervised **TCN / video behavior classifiers**.

```{figure} ../images/showcase/behavior_scoring_timeline.gif
---
name: behavior-scoring-gif
alt: Animated demonstration of scoring timestamped behavior bouts directly inside the Annolid GUI
width: 90%
---
Interactive behavior scoring inside Annolid: mark start and stop timestamps while scrubbing your video, and export clean bout tables and ethogram plots.
```

## Shared Project Schema (`project.annolid.json`)

Define your ethogram behaviors **once** — Annolid automatically keeps names synchronized across:

- the **Flags** dock (per-frame & start/stop scoring),
- the **Timeline** dock (interactive drag-scrubbing needle + resizable bout bars),
- **Annolid Bot** (1-second automated segment classification), and
- **BORIS** bidirectional import/export.

```{figure} ../images/showcase/mouse083_ethogram_kinematics.png
---
name: behavior-ethogram-output
alt: Scored behavior ethogram timeline raster paired with inter-animal distance curve, trajectories, and behavior time budget
width: 96%
---
Downstream ethogram raster, proximity alignment, and behavior time budget computed from Annolid behavior labels on `mouse083_task1_annotator1`.
```

## Workflow 1: Manual Scoring With Flags & Timeline (Fastest Start)

1. Open your video in Annolid (or pre-populate behaviors from the terminal with `annolid --flags "investigation,mount,grooming,rearing"`).
2. Open the **Flags** dock and add your behavior names, then click **Save All** (`Ctrl+S`).
3. Open the **Timeline** dock:
   - Drag the **red timeline playhead needle** to scrub frames continuously.
   - Click **Start / End** in Flags (or create/drag interval bars on the Timeline) to record bouts.
4. Export behavior events to CSV and compute a full **time budget** + ethogram SVG + transition graph:

```bash
# Compute bout counts, total/mean/median durations, 60s binned time course, and SVG plots
annolid-run time-budget exported_events.csv \
  --schema project.annolid.json \
  --bin-size 60 \
  --ethogram-svg ethogram.svg \
  --transitions-svg transitions.svg \
  -o time_budget.csv
```

```{note}
Classic helper syntax also remains supported: `python -m annolid.behavior.time_budget /path/to/exported_events.csv --bin-size 60 -o time_budget.csv`.
```

## Workflow 2: Agent-Assisted 1-Second Segment Labeling (Annolid Bot)

Once your behaviors are defined in the project schema, let **Annolid Bot** draft a first-pass ethogram over 1-second video windows using a multimodal vision-language model (local Ollama or hosted VLM):

1. Open **`AI & Models → Annolid Bot…`** (or click **`Label 1s Behaviors`** in the Bot dock).
2. Paste a structured prompt:

```text
Label behavior in /path/to/video.mp4 with labels grooming, rearing, investigation every 1s
```

Or provide rich domain definitions for subtle social assays:

```text
Label behavior in /path/to/video.mp4 with labels aggression_bout every 1s
video description: Two mice in resident-intruder home cage;
instances: 2;
behavior definitions: Aggression bout includes lunging, chasing, or physical wrestling;
focus points: Count bouts and note onset/offset transition frames.
```

Annolid constrains the model to strict JSON (`label`, `confidence`, `description`) and writes reviewable timeline intervals, behavior timestamps CSV, and a segment-level JSON log so you can inspect and adjust every bout on the Timeline!

## Workflow 3: Bidirectional BORIS & Inter-Rater Reliability

Already score videos in **BORIS**? Round-trip cleanly without losing modifiers or out-of-sight intervals:

```bash
# Import a .boris project into Annolid events + cohort manifest
annolid-run boris-import study.boris --output-dir ./annolid_from_boris --group-variable Treatment

# Export Annolid behavior events back to a .boris file
annolid-run boris-export session_events.csv --schema project.annolid.json --format boris --output session.boris

# Measure inter-rater agreement (Cohen's kappa, Fleiss' kappa, Krippendorff's alpha)
annolid-run behavior-irr rater1.csv rater2.csv --bin-seconds 0.1 --disagreements-csv disagreements.csv --out irr.json
```

## Workflow 4: Train a Supervised Behavior Classifier (Optional)

For labs with labeled multi-video behavior corpora, Annolid also ships polygon-feature **TCN (Temporal Convolutional Network)** and video behavior classification utilities under `annolid/behavior/`:

```bash
python -m annolid.behavior.training.train --video_folder /path/to/labeled_clips
```

```{tip}
Want copy-paste Annolid Bot prompt recipes or TCN pipeline details? See [Behavior Labeling with Timeline, Flags, and Bot](https://annolid.com/portal/tutorials/behavior_timeline_flags_bot/) and [TCN Behavior Classification](https://annolid.com/portal/tutorials/tcn_behavior_pipeline/) on the Docs Portal.
```
