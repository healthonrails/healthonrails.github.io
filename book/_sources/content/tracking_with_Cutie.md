# Tracking From One Frame with Cutie

This step-by-step guide walks you through Annolid's signature **zero-training workflow**: outline your animals on **one frame** with AI-Polygons, launch **Cutie** video object segmentation (VOS), verify predictions in real time, fix any occlusion mistake in seconds, and export clean tracking CSVs.

```{tip}
Want to see how Cutie fits into a complete 4,881-frame social behavior assay with 14 keypoints, automated Track QC, spatial zones, and an HTML5 report? Check out the [Featured Walkthrough (`mouse083`)](../tutorials/mouse083_resident_intruder_showcase.md)!
```

For full methodological details on Annolid's SAM / Grounding DINO + Cutie tracking pipeline, see [Yang & Cleland, 2024](https://arxiv.org/abs/2403.18690) and [Yang et al., 2023](https://arxiv.org/abs/2312.07723).

## Step 1: Open Your Video & Label One Seed Frame

1. Launch `annolid` and click **`Open Video`** on the toolbar (or **`File → Open Video`**).
2. Scrub to a clean starting frame where every animal and object you want to track is clearly visible and separated.
3. Right-click on the canvas and select **`Create AI-Polygon`**. Click each object to let Segment Anything snap a tight polygon around it.

```{figure} ../images/AI_polygon.png
---
name: cutie-step1-ai-polygon
alt: Opening a video in Annolid and selecting Create AI-Polygon from the context menu
width: 94%
---
**Step 1a:** Right-click on a clean seed frame and pick **Create AI-Polygon** to outline each target with a single click.
```

4. Hold **`Ctrl` (macOS `Cmd`) + Left-Click** to finish each polygon and assign a unique instance name (for example `mouse_1`, `mouse_2`, `teaball`).
5. Press **`Ctrl+S`** (`Cmd+S` on macOS) or click **Save** to write the seed frame JSON to disk.

```{figure} ../images/click_save_polygon.png
---
name: cutie-step1-save-label
alt: Labeling an AI-generated polygon in Annolid using Ctrl+Click and saving to JSON
width: 94%
---
**Step 1b:** Name each instance cleanly and save your seed frame (`Ctrl+S`) before starting prediction.
```

## Step 2: Start Automatic Tracking (`Pred`)

1. Choose **`Cutie`** from the **AI Model** dropdown in the top toolbar.
2. Click the green **`Pred`** button.
3. Annolid tracks forward in a background worker thread so the UI remains responsive. Drag the bottom video slider at any time to inspect completed frames as they stream in.

```{figure} ../images/stop_prediction_and_correction.png
---
name: cutie-step2-running
alt: Cutie tracking running in the background inside Annolid while reviewing completed frames
width: 94%
---
**Step 2:** Cutie propagates every labeled instance mask forward automatically while you monitor progress live.
```

```{note}
**Self-healing runtime:** If a Cutie dependency is missing in a lean `annolid[gui]` install, Annolid can automatically install the missing packages (or display the exact `pip install` command when `ANNOLID_AUTO_INSTALL_CUTIE_DEPS=0` is set).
```

## Step 3: Pause, Correct an Anchor Frame & Resume

If two animals cross closely or a sudden occlusion causes drift on a later frame:

1. Click the red **`Stop`** button to pause tracking.
2. Scrub back to the **first frame** where the mask drifted or swapped IDs.
3. Fix that single frame using **Edit Polygons** or **Create AI-Polygon** and press **`Ctrl+S`**.
4. Clear stale predictions after that frame and click **`Pred`** again — Cutie resumes cleanly forward from your corrected anchor!

```{figure} ../images/delete_prediction_from_next_frame.png
---
name: cutie-step3-correct
alt: Pausing tracking, correcting a single anchor frame, and deleting stale future predictions
width: 94%
---
**Step 3:** Correct only the first frame where an error begins, prune stale future predictions, and resume forward.
```

## Step 4: Review & Finalize Predictions

When tracking reaches the end of the video, scrub through key interactions — or run automated **Track QC** (`Analysis → Analysis & Reporting Studio…`) to let Annolid highlight any short dropout or velocity spike automatically!

```{figure} ../images/check_and_finish_prediction.png
---
name: cutie-step4-finish
alt: Reviewing finalized multi-frame Cutie tracking predictions in Annolid
width: 94%
---
**Step 4:** Verify your tracked masks across the recording and export summary tables.
```

## Where Your Tracking Outputs Are Saved

Annolid saves results into a sibling folder matching your video's name (`<video_stem>/`):

- **Manual seed & corrected frames**: `<video_stem>_#########.json` (LabelMe JSON)
- **High-volume predicted frames**: per-frame JSON files or compact `<video_stem>_annotations.ndjson` (`AnnotationStore`)
- **Summary spreadsheets**:
  - `<video_stem>_tracking.csv` — per-frame RLE masks, bounding boxes, and centroids for every shape
  - `<video_stem>_tracked.csv` — clean per-instance centroid trajectories, motion indices, and timestamps ready for Python, R, or `annolid-run report`

## References

- [1] C. Yang and T. A. Cleland, *"Annolid: Annotate, Segment, and Track Anything You Need,"* [arXiv:2403.18690](https://arxiv.org/abs/2403.18690), 2024.
- [2] C. Yang, J. Forest, M. Einhorn, and T. A. Cleland, *"Automated Behavioral Analysis Using Instance Segmentation,"* [arXiv:2312.07723](https://arxiv.org/abs/2312.07723), 2023.
- [3] J. Fang, C. Yang, and T. A. Cleland, *"Scoring rodent digging behavior with Annolid,"* Soc. Neurosci. Abstr. 512.01, 2023.

Next: for very long videos with repeated disappearances or text-prompted seeding, check out [Long-Video Tracking with SAM3](../tutorials/SAM3_video_tracking.md).
