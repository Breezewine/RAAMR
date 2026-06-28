"""General image preprocessing utilities used by the public RAAMR templates."""

from __future__ import annotations

from pathlib import Path
from typing import Tuple

import numpy as np
from PIL import Image

try:
    import cv2
except Exception:  # pragma: no cover
    cv2 = None


def resize_keep_ratio_and_pad(gray: np.ndarray, target_h: int, target_w: int) -> np.ndarray:
    """Resize a 2D grayscale image while preserving aspect ratio, then center-pad."""
    if gray.ndim != 2:
        raise ValueError("Expected a 2D grayscale image.")

    h, w = gray.shape
    scale = min(target_h / max(h, 1), target_w / max(w, 1))
    new_h = max(1, int(round(h * scale)))
    new_w = max(1, int(round(w * scale)))

    pil = Image.fromarray(gray.astype(np.uint8))
    resized = np.asarray(pil.resize((new_w, new_h), Image.BILINEAR), dtype=np.uint8)

    canvas = np.zeros((target_h, target_w), dtype=np.uint8)
    y0 = (target_h - new_h) // 2
    x0 = (target_w - new_w) // 2
    canvas[y0 : y0 + new_h, x0 : x0 + new_w] = resized
    return canvas


def apply_clahe_gray(gray: np.ndarray, clip_limit: float = 2.0, tile_grid_size: Tuple[int, int] = (8, 8)) -> np.ndarray:
    """Apply CLAHE to a uint8 grayscale image."""
    gray_u8 = gray.astype(np.uint8)
    if cv2 is None:
        return gray_u8
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=tile_grid_size)
    return clahe.apply(gray_u8)


def load_gray_image(path: str | Path, target_h: int = 1024, target_w: int = 768, apply_clahe: bool = True) -> np.ndarray:
    """Load an image as normalized grayscale in [0, 1]."""
    image = Image.open(path).convert("L")
    arr = np.asarray(image, dtype=np.uint8)
    arr = resize_keep_ratio_and_pad(arr, target_h=target_h, target_w=target_w)
    if apply_clahe:
        arr = apply_clahe_gray(arr)
    return arr.astype(np.float32) / 255.0

