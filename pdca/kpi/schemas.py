from dataclasses import dataclass
from typing import Generator

from .models import KPIConfig, KPIValue


@dataclass
class MatrixValue:
    kpi: int
    phase: int
    is_glide: bool
    real_val: KPIValue | None


@dataclass
class MatrixItem:
    kpi: KPIConfig
    value: Generator[MatrixValue, None, None]
