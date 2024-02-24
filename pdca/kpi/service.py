from typing import List, Union

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet

from .repository import DepartmentRepositoryInterface, KPIRepositoryInterface
from .models import Department


class DepartmentService:
    def __init__(self, repository: DepartmentRepositoryInterface) -> None:
        self.repository = repository

    def fetch_all(self) -> Union[QuerySet, List[Department], None]:
        return self.repository.fetch_all()

    def fetch_one(
        self, search_string: str, is_slug: bool = False
    ) -> Union[Department, None]:
        if is_slug:
            return self.repository.fetch_by_slug(search_string)
        else:
            return self.repository.fetch_by_title(search_string)


class KPIservice:
    def __init__(self, repository: KPIRepositoryInterface) -> None:
        self.repository = repository

    def get_kpi_matrix(
        self, search_string: str, is_glide: bool = False
    ) -> tuple | None:
        self.departmet = DepartmentService()._get_department
        kpis = self.repository.fetch_all_kpis_by_department(search_string, slug=True)
        phases = self.repository.get_phases()
        if not kpis or not phases:
            return None
        body = self._generate_matrix_body(kpis, phases)
        phases_titles = phases.values_list("title", flat=True)
        header = ("KPI", "Entity", "Category", *phases_titles)
        return header, body

    # def _generate_matrix_body(self, kpis, phases):
    #     kpivalues = none

    #     return 0

    # def generate_body_item(
    #     self, phase: KPIPhase, kpi: KPIConfig, is_glide: bool = False
    # ) -> MatrixValue:
    #     real_val = self._fetch_kpi_value_by_phase_and_config(
    #         phase=phase, kpi=kpi, is_glide=is_glide
    #     )
    #     return MatrixValue(kpi.id, phase.id, is_glide, real_val)
