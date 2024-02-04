from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from .schemas import MatrixItem


from .repository import KPIRepository, DepartmentRepository
from .models import Department, KPIConfig


__all__ = ["DepartmentService", "KPIservice"]


class DepartmentService:
    def __init__(self) -> None:
        self.repository = DepartmentRepository()

    def fetch_all(self) -> None | QuerySet | List[Department]:
        try:
            return self.repository.fetch_all()
        except ObjectDoesNotExist:
            return None

    def fetch_one(self, search_string: str, is_slug: bool = False):
        try:
            if is_slug:
                res = self.repository.fetch_one_by_slug(search_string)
            else:
                res = self.repository.fetch_one_by_title(search_string)
            return res
        except ObjectDoesNotExist:
            return None


class KPIservice:
    def __init__(self) -> None:
        self.repository = KPIRepository()

    def get_kpi_matrix(self, search_string: str, is_glide=False) -> QuerySet:
        kpis = self.repository.fetch_all_kpis_by_department(
            search_string, slug=True
        )
        phases = self.repository.get_phases()
        body = []
        for kpi in kpis:
            row = [self.repository.generate_body_item(phase, kpi, is_glide) for phase in phases]
            item = MatrixItem(kpi, row)
            body.append(item)
        
        phases = phases.values_list("title", flat=True)
        header = ("KPI", "Entity", "Category",*phases)
        return (header, body)
