# Running Annolid on Google Colab

No local NVIDIA GPU? **Google Colab Studio** lets you run GPU-heavy Annolid training and inference (**YOLO11/YOLO26**, **DINO KPSEG**, **Mask R-CNN**, **Keypoint R-CNN**, **Sim-to-Real loops**, and video batch tracking) on cloud T4/L4/A100 GPUs directly from the Annolid desktop app or CLI.

## Launch Google Colab Studio

- **From the Annolid GUI**: Open **`AI & Models → Google Colab…`**, click the **Google Colab** toolbar button, or click **`Run on Google Colab…`** inside the **Training Wizard**, **Inference Wizard**, or **Sim-to-Real Studio**.
- **From the CLI (`annolid-run colab`)**:

```bash
# Check authentication and available Colab runtime status
annolid-run colab status
annolid-run colab auth login

# Train a YOLO11 segmentation model on a Colab T4 GPU
annolid-run colab train yolo \
  --data /path/to/data.yaml \
  --weights yolo11s-seg.pt \
  --gpu T4

# Run remote YOLO inference and pull LabelMe JSONs back locally
annolid-run colab predict yolo_labelme \
  --source /path/to/video.mp4 \
  --weights /path/to/best.pt \
  --gpu T4
```

## Official Ready-to-Run Colab Notebooks

Click any badge to launch directly in Google Colab:

| Workflow | Launch in Colab |
| --- | --- |
| **Unified Annolid Train & Inference *(Recommended)*** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/healthonrails/annolid/blob/main/docs/tutorials/Annolid_Colab_Train_and_Inference.ipynb) |
| **YOLO Instance Segmentation** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/healthonrails/annolid/blob/main/docs/tutorials/Annolid_Instance_Segmentation_on_YOLO_Tutorial.ipynb) |
| **YOLO Pose Estimation** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/healthonrails/annolid/blob/main/docs/tutorials/Annolid_Pose_Estimation_on_YOLO_Tutorial.ipynb) |
| **Legacy Detectron2 Mask R-CNN** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/healthonrails/annolid/blob/main/docs/tutorials/Annolid_on_Detectron2_Tutorial.ipynb) |

## End-to-End Cloud Workflow

1. **Label locally in Annolid** and export a dataset (YOLO `data.yaml`, LabelMe `spec.yaml`, or COCO folder) — or let **Sim-to-Real Studio** generate one automatically.
2. **Sign in once** via **Google Colab Studio** or `annolid-run colab auth login` (supports `google-colab-cli`, Google OAuth2 for Colab API + Drive, or `gcloud` ADC).
3. **Dispatch training or inference** directly to a remote GPU (`cli` / `api` backend) or generate a Google Drive-synced `.ipynb` notebook (`notebook` backend).
4. **Pull artifacts back & review**: Trained `best.pt` weights, training metrics (viewable in **Training Monitor `Ctrl+Shift+V`**), and predicted LabelMe JSONs / tracking CSVs download locally (or pull anytime with `annolid-run colab pull <job_id>`).

```{tip}
Need detailed OAuth setup instructions, Drive sync tips, or Annolid Bot cloud-job prompts? See the full [Google Colab Guide](https://annolid.com/portal/google_colab/) on the Annolid Docs Portal.
```
