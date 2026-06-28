"""Public model interface placeholder.

The complete RAAMR architecture is not included in this verification-oriented
repository. This stub documents the expected input and output contract used by
the evaluation scripts and by the private training implementation.
"""

from __future__ import annotations

from typing import Dict

import torch
from torch import nn


class RAAMRModel(nn.Module):
    """Interface placeholder for the private RAAMR implementation."""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
        self.release_note = (
            "The full architecture is omitted from the public release. "
            "This class only documents the expected forward interface."
        )

    def forward(self, batch: Dict[str, torch.Tensor]) -> Dict[str, torch.Tensor]:
        """Return patient-level logits and auxiliary outputs.

        Expected private output keys:
            patient_logit: Tensor with shape [B]
            probability: Tensor with shape [B]
            reliability_score: optional Tensor with shape [B]
        """
        raise NotImplementedError(
            "The private RAAMR model implementation is not included in this public repository."
        )

