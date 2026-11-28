# Long-Video Tracking & Correction with SAM3

**SAM3 / SAM3.1** in Annolid brings promptable, long-horizon video segmentation and tracking — supporting both **geometric seeds** (polygons, boxes, or points) and **natural-language text prompts**, plus an agentic windowed tracker (**SAM3 Agent**) that re-anchors across long videos and repairs gaps in existing NDJSON tracks.

## When to Choose SAM3 vs. Cutie

| Scenario | Recommended Backend |
| --- | --- |
| Short-to-medium clip with 1 clean seed frame | **[Cutie](../content/tracking_with_Cutie.md)** (fast, lightweight) |
| Long video where animals hide and re-appear | **SAM3 / SAM3 Agent** (windowed overlap carry-over) |
| Zero manual drawing — track directly from text (`mouse`, `black mouse=resident`) | **SAM3 Text-Only Mode** |
| Repairing missed frames or short ID swaps in an existing `*_annotations.ndjson` | **SAM3 Agent Correction via Annolid Bot** |

## Prerequisites

Install Annolid with the `sam3` extra (or use the `workstation` installer profile):

```bash
pip install "annolid[gui,sam3]"
# Or from a local checkout:
pip install -e ".[gui,sam3]"
```

Or install on demand via `annolid-run runtime install sam3`.

## Mode 1: Seeded Tracking (Polygons, Boxes, or Points)

1. Open your video in Annolid (`File → Open Video`).
2. Annotate one or more objects on a clear starting frame using polygons, rectangles, or points, then press **`Ctrl+S`**.
3. Select **SAM3** in the **AI Model** dropdown.
4. Click **`Pred`** — Annolid converts your polygon or box prompts into SAM3 mask seeds and propagates them cleanly across frames.

## Mode 2: Text-Prompted Tracking (Zero Drawing)

When no geometric shapes exist on the starting frame, SAM3 can segment and track purely from text phrases:

1. Enter one or more phrases in the toolbar **Text Prompt** field, separated by commas, semicolons, periods, or new lines — for example:
   - `mouse`
   - `black mouse=resident, white mouse=intruder`
   - `black mouse -> resident; white mouse -> intruder`
2. Annolid strips optional `query=label` / `query -> label` aliases down to the visual query text for SAM3 while saving the resulting polygons under your clean study label names!
3. Select **SAM3** and click **`Pred`** (or type `/track` in Annolid Bot).

## Mode 3: Fast GUI Chat With `/track`

Inside the **Annolid Bot** dock (`AI & Models → Annolid Bot…`), type `/track` with no arguments to open a guided tracking form, or paste a structured command directly:

```text
/track
/track video=/path/to/video.mp4 prompt="mouse" model=SAM3
/track video=/path/to/video.mp4 prompt="black mouse=resident, white mouse=intruder" model=SAM3 to_frame=600
```

```{figure} ../images/showcase/annolid_bot_gui_dock.png
---
name: sam3-bot-dock
alt: Annolid Bot dock in the GUI where /track and SAM3 Agent commands can be launched
width: 84%
---
Type `/track` in the **Annolid Bot** dock to launch guided Cutie or SAM3 tracking with clear model and frame-range controls.
```

## Mode 4: Long-Video Agent Tracking & Occlusion Repair

For very long recordings or repeated occlusions, **SAM3 Agent** (`sam3_agent_video_track`) breaks the video into overlapping windows, refines seeds between windows, and preserves identities across re-entries:

1. First run a quick **dry run** in Annolid Bot to confirm paths and window settings:
   ```text
   sam3_agent_video_track(
     video_path="/path/to/video.mp4",
     agent_prompt="mouse",
     window_size=5,
     stride=5,
     propagation_direction="forward",
     dry_run=true
   )
   ```
2. Once verified, rerun with `dry_run=false`.
3. Annolid writes a reviewable `<video_stem>_sam3_agent/` output folder and `<video_stem>_sam3_agent_tracking.json` summary (`frames_processed`, `masks_written`, resolved config).

```{tip}
**Repairing an existing track without starting over:** If Track QC spots a short dropout or ID swap inside an existing `*_annotations.ndjson`, Annolid Bot can run SAM3 Agent strictly over the problematic frame span and merge the repaired masks into a reviewable corrected NDJSON copy. See the full [SAM3 Guide](https://annolid.com/portal/sam3/) and [SAM3 Bot Correction Tutorial](https://annolid.com/portal/tutorials/tracking_correction_with_sam3_bot/) on the Docs Portal.
```
