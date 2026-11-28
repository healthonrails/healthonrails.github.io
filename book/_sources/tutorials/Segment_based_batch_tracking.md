# Segment-Based Batch Tracking & Long-Video Scale-Up

Tracking a 30-second clip interactively is easy — tracking **20 hour-long recordings** overnight without drift or wasted compute takes **Segment-Based Batch Tracking**.

Annolid's **Video Manager** + **Define Video Segments** (`Ctrl+Alt+S`) workflow lets you split long videos into bounded tracking windows anchored by saved manual seed frames, then run **`Track All`** unattended across an entire folder.

```{figure} ../images/diagrams/segment_batch_tracking_animation.gif
---
name: seg-batch-animation
alt: Animated 4-stage diagram showing manual anchor seed frames resetting tracking windows across a long video
width: 96%
---
Every saved manual seed frame acts as a hard reset point: Cutie tracks from one seed up to the frame before the next seed without overwriting your manual ground truth.
```

## Step-by-Step Batch Workflow

### 1. Queue Your Folder in Video Manager
1. Open the **Video List** dock on the right side of the Annolid window.
2. Click **`Import…`**, select your experiment folder, and click **Load** on the first video.

### 2. Label Seed Frames & Define Segments (`Ctrl+Alt+S`)
1. Scrub to the starting frame of your first window, outline your animals, and save (`Ctrl+S`) to write a PNG+JSON seed pair.
2. Open **`Video Tools → Define Video Segments…`** (`Ctrl+Alt+S`).
3. Click **`Use Annolid Frame`** to capture the current frame number, choose an end condition (*Duration*, *End Time*, or *End Frame*), and click **`Add Segment`**.
4. Repeat for any additional segments or tricky intervals, then click **`OK`**. Annolid saves your plan to `<video>.segments.json` so it restores automatically next time.

### 3. Run `Track All` Unattended
1. Repeat Step 2 for any other videos in the queue (videos without saved segments automatically fall back to whole-video tracking).
2. Click **`Track All`** in Video Manager. Annolid steps cleanly through every queued video and segment, writing per-frame annotations, tracking CSVs, and optional gap reports.

## Repairing Cutie ID Switches With Manual Seed Anchors

This is the fastest, most reliable way to repair an identity swap in home-cage multi-animal recordings:

1. Use **[Track QC](Reporting_and_track_qc.md)** (or scrub to the first crossing) to find the **first frame** where two animals swapped labels.
2. Fix the labels/polygons on that single frame and press **`Ctrl+S`**.
3. Rerun Cutie from that corrected frame (or define a segment ending right before the next already-correct seed).
4. **Why it works so cleanly**: Manual seed frames supersede automatic predictions — Annolid never overwrites saved manual frames, and Cutie automatically breaks long runs into independent windows from seed to seed.

```{tip}
**Opt-in Identity-Switch Pause:** For extra-sensitive recordings, programmatic/advanced runs can set `identity_switch_protection=True`. Rather than guessing and silently swapping labels, Annolid pauses before saving a suspicious crossing frame so you can verify identities, save a clean seed, and continue!
```

## Cleanly Retracking a Video Without Losing Manual Labels

Want a fresh tracking pass while keeping every frame you labeled by hand?

::::{dropdown} Which generated files to delete vs. keep before retracking
**Safe to delete (auto-generated outputs):**
- `<video_name>*_tracking.csv` and `<video_name>*_tracked.csv`
- `<video_name>*_gaps_report.csv` and `<video_name>*_tracking_gaps_report.md`
- `<video_name>/<video_name>_annotations.ndjson` *(if present)*

**Keep intact inside `<video_name>/`:**
- Your manually labeled `.png` images and matching `.json` seed files!

Then reopen the video in Annolid and rerun tracking — Annolid immediately picks up all your saved manual seeds.
::::

For advanced throughput tuning and segment JSON schemas, see [Segment-Based Batch Tracking](https://annolid.com/portal/tutorials/segment-based-batch-tracking/) on the Docs Portal.
