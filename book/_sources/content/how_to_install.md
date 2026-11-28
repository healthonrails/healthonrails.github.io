# Installation Options

Annolid exposes two primary commands after installation:

- **`annolid`** — launches the interactive Qt desktop GUI
- **`annolid-run`** — runs tracking, training, Track QC, zone analysis, pose interoperability, Sim-to-Real, and HTML5 reporting from the terminal

Annolid requires **Python 3.10+** (Python **3.11 or 3.12** is recommended for shared lab workstations).

```{tip}
Looking for exhaustive installer flags, ONNX GPU troubleshooting, or air-gapped wheelhouse details? See the canonical [Installation Guide](https://annolid.com/portal/installation/), [One-Line Installer Choices](https://annolid.com/portal/one_line_install_choices/), and [uv Setup Guide](https://annolid.com/portal/install_with_uv/) on the Annolid Docs Portal.
```

## Quick Install (Pick Your Platform & Method)

::::{tab-set}

:::{tab-item} macOS / Linux (One-Line)
Recommended for most users — creates an isolated environment, checks GPU/ONNX acceleration, and creates desktop **Launch** and **Update** shortcuts:

```bash
# Lean default GUI install (fastest)
curl -sSL https://raw.githubusercontent.com/healthonrails/annolid/main/install.sh | bash

# Full lab workstation profile (GUI + Cutie + SAM3 + training + 3D viewers)
curl -sSL https://raw.githubusercontent.com/healthonrails/annolid/main/install.sh | bash -s -- --profile workstation

# Non-interactive CPU baseline
curl -sSL https://raw.githubusercontent.com/healthonrails/annolid/main/install.sh | bash -s -- --no-gpu --no-interactive
```
:::

:::{tab-item} Windows (PowerShell)
Run in PowerShell — creates an isolated environment plus double-click `Launch Annolid.cmd` and `Update Annolid.cmd` shortcuts:

```powershell
# Lean default GUI install
irm https://raw.githubusercontent.com/healthonrails/annolid/main/install.ps1 | iex

# Non-interactive CPU baseline
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/healthonrails/annolid/main/install.ps1))) -NoGpu -NoInteractive
```
:::

:::{tab-item} pip (PyPI)
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install "annolid[gui]"
annolid
```

Install optional ML runtimes anytime via `Settings → Runtime & Optional Packages…` or:
```bash
annolid-run runtime status
annolid-run runtime install tracking sam3
```
:::

:::{tab-item} uv (Developer Checkout)
```bash
git clone --recurse-submodules https://github.com/healthonrails/annolid.git
cd annolid
uv venv .venv --python 3.11
source .venv/bin/activate
uv pip install -e ".[gui]"
```
:::

:::{tab-item} Conda
```bash
conda create -n annolid-env python=3.11
conda activate annolid-env
conda install -c conda-forge git ffmpeg
git clone --recurse-submodules https://github.com/healthonrails/annolid.git
cd annolid
pip install -e ".[gui]"
annolid
```
:::

:::{tab-item} Air-Gapped / Offline
```bash
# 1. On an online machine matching OS/Python: export checksummed wheelhouse
annolid-run runtime bundle --profile workstation --out ./annolid-wheelhouse

# 2. On the offline lab machine: verify SHA256 manifest and install
annolid-run runtime verify-bundle ./annolid-wheelhouse
annolid-run runtime install --profile workstation --wheelhouse ./annolid-wheelhouse --offline
```
:::

:::{tab-item} Docker (Linux X11)
```bash
cd annolid/docker
docker build -t annolid .
xhost +local:docker
docker run -it -v /tmp/.X11-unix:/tmp/.X11-unix/ -e DISPLAY=$DISPLAY annolid
```
:::

::::

### Choose an Installer Profile

| Profile | Included Capabilities | Best For |
| --- | --- | --- |
| `gui` *(default)* | Lean desktop GUI (`PySide6-Essentials`), annotation, zones, CSV/COCO/YOLO export | Quickest setup; laptops; light labeling |
| `tracking` | GUI + `ml`, `tracking`, `cutie` | Single-frame video tracking & DINOv3 keypoints |
| `workstation` | GUI + `ml`, `tracking`, `cutie`, `sam3`, `training`, `webengine`, `pdf` | Full lab analysis workstation + 3D viewers |
| `full` | GUI + `all` extras | Every optional integration & Annolid Bot plugins |

### Launching & Updating Without the Terminal

After a one-line venv install, open the install folder and double-click:

| Platform | Launch Annolid | Update Annolid |
| --- | --- | --- |
| **macOS** | `Launch Annolid.command` | `Update Annolid.command` |
| **Windows** | `Launch Annolid.cmd` | `Update Annolid.cmd` |
| **Linux** | `Launch Annolid.desktop` | `Update Annolid.desktop` |

## Verify Your Installation (30-Second Check)

Run these three commands in your activated environment:

```bash
annolid --version
annolid-run --help
annolid-run list-models
```

Then launch the desktop application:

```bash
annolid
```

```{figure} ../images/showcase/mouse083_gui_workspace.png
---
name: install-gui-preview
alt: Annolid desktop GUI open on a tracked home-cage mouse video with Flags, Label Instances, and Video List docks
width: 96%
---
A healthy Annolid desktop session with video canvas, polygon and keypoint overlays, behavior status pill, and right-hand workspace docks.
```

## Quick Troubleshooting

- **`qtpy.QtBindingsNotFoundError`**: Make sure you installed the `gui` extra (`pip install "annolid[gui]"`).
- **Missing video codecs or FFmpeg errors**: Install FFmpeg (`brew install ffmpeg` on macOS, `conda install -c conda-forge ffmpeg`, or your Linux package manager).
- **Do I need Detectron2?** No! Modern Annolid workflows (SAM AI-Polygons, Cutie, SAM3, DINOv3, INSID3, YOLO11/YOLO26, zones, Track QC, and HTML5 reports) do **not** require Detectron2. Only legacy Mask R-CNN Detectron2 notebooks need it, and those run easiest on [Google Colab](Annolid_on_Google_Colab.md).

Next up: learn how to [prepare and compress your videos](video_preparation.md) for fast, crisp tracking.
