# RAAMR

This repository provides a lightweight public release for the manuscript:

**RAAMR: Reliability-Aware Asymmetric Multimodal Representation Learning for Mammography Classification**

RAAMR is designed for patient-level breast mammography classification under realistic multimodal availability. The study uses four-view FFDM images, DBT-derived 2D images when available, and structured report semantics extracted from clinical radiology reports. The public repository is intended to support reproducibility checks, data-format transparency, metric verification, and figure-generation workflows.

> Note: The full model implementation, training objectives, checkpoints, and private clinical data are not included in this public release because the manuscript is under review and the work involves ongoing intellectual-property protection and restricted clinical data. The complete training code can be made available to reviewers under a confidential review process or released after publication according to the final data and code-sharing policy.

## What is included

- Data schema for patient-level multimodal mammography experiments.
- Safe preprocessing utilities for FFDM and DBT-derived 2D images.
- Structured-report parsing templates without private patient content.
- Example configuration files with placeholder paths.
- Repository structure suitable for linking in a paper submission.

## What is not included

- The full RAAMR model architecture.
- The private Meta-Net, adaptive prompting, reliability routing, and fusion implementation.
- Training checkpoints and pretrained weights.
- Private FFDM, DBT, or pathology-report data.
- Patient identifiers or real clinical report text.

These components are intentionally omitted from the public release. The repository still exposes the experimental interface and evaluation protocol so that readers can inspect how inputs, outputs, and reported metrics are organized.

## Repository layout

```text
RAAMR_public_release/
  README.md
  requirements.txt
  .gitignore
  configs/
    example_config.yaml
  data/
    README.md
  examples/
    predictions_template.csv
    structured_report_template.json
  raamr/
    __init__.py
    data_schema.py
    model_stub.py
    preprocessing.py
```

## Data organization

The internal experiments use patient-level samples. Each patient can contain up to four FFDM views and optional DBT-derived 2D views.

Expected FFDM view names:

- `L_CC`
- `R_CC`
- `L_MLO`
- `R_MLO`

Expected sample-level metadata:

```csv
patient_id,label,split,L_CC,R_CC,L_MLO,R_MLO,DBT_L_CC,DBT_R_CC,DBT_L_MLO,DBT_R_MLO,report_json_id
P000001,1,test,/path/L_CC.png,/path/R_CC.png,/path/L_MLO.png,/path/R_MLO.png,/path/dbt_lcc.png,,,,P000001
```

Labels are binary:

- `0`: benign or non-malignant
- `1`: malignant

The public template intentionally uses placeholder paths. Do not upload private image paths or patient identifiers to a public repository.

## Structured report template

The full study uses structured report semantics extracted from Chinese clinical reports. In the private workflow, Chinese reports are summarized and normalized into structured fields before being used by the multimodal model. A public template is provided in `examples/structured_report_template.json`.

Example fields:

- `patient_id`
- `side`
- `birads`
- `mass`
- `calcification`
- `distortion`
- `asymmetry`
- `summary`

The template is only a schema example and does not contain patient data.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Minimal usage

The public release is intended to document the experimental interface rather than to reproduce the private training pipeline. Users can inspect the data schema, structured-report template, preprocessing utilities, and model input-output contract.

## Citation

If you use this repository, please cite the manuscript after it becomes available.

```bibtex
@misc{raamr2026,
  title  = {RAAMR: Reliability-Aware Asymmetric Multimodal Representation Learning for Mammography Classification},
  author = {Anonymous Authors},
  year   = {2026},
  note   = {Manuscript under review}
}
```

## Code release policy

This public repository is a verification-oriented release. It supports transparency in preprocessing, data organization, and metric reporting while protecting the unpublished core algorithm. Full release scope will be updated after peer review and according to institutional data-governance requirements.
