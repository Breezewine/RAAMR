"""Schema checks for public RAAMR data templates."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

import pandas as pd


REQUIRED_METADATA_COLUMNS = ["patient_id", "label", "split", "L_CC", "R_CC", "L_MLO", "R_MLO"]
OPTIONAL_DBT_COLUMNS = ["DBT_L_CC", "DBT_R_CC", "DBT_L_MLO", "DBT_R_MLO"]
REQUIRED_REPORT_FIELDS = ["patient_id", "side", "summary"]


def missing_columns(columns: Iterable[str], required: Iterable[str]) -> List[str]:
    present = set(columns)
    return [col for col in required if col not in present]


def validate_metadata_csv(path: str | Path) -> pd.DataFrame:
    """Validate a patient-level metadata CSV and return the loaded frame."""
    df = pd.read_csv(path)
    missing = missing_columns(df.columns, REQUIRED_METADATA_COLUMNS)
    if missing:
        raise ValueError(f"Missing required metadata columns: {missing}")

    invalid_labels = sorted(set(df["label"].dropna().astype(int)) - {0, 1})
    if invalid_labels:
        raise ValueError(f"Labels must be binary 0/1; found: {invalid_labels}")

    invalid_splits = sorted(set(df["split"].dropna().astype(str)) - {"train", "val", "test"})
    if invalid_splits:
        raise ValueError(f"Split values must be train/val/test; found: {invalid_splits}")
    return df


def validate_structured_report_json(path: str | Path) -> list:
    """Validate a structured report JSON template."""
    with open(path, "r", encoding="utf-8") as f:
        records = json.load(f)

    if not isinstance(records, list):
        raise ValueError("Structured report JSON must be a list of records.")

    for idx, rec in enumerate(records):
        if not isinstance(rec, dict):
            raise ValueError(f"Record {idx} is not a JSON object.")
        missing = missing_columns(rec.keys(), REQUIRED_REPORT_FIELDS)
        if missing:
            raise ValueError(f"Record {idx} missing required fields: {missing}")
    return records

