from typing import List

from django.db.models import QuerySet

from .schemas import MatrixValue

from .exceptions import NotTitleError
from .models import Department, KPIConfig, KPIPhase, KPIValue


class DepartmentRepository:
    @staticmethod
    def fetch_all():
        return Department.objects.filter(is_active=True)

    @staticmethod
    def fetch_one_by_title(title):
        return Department.objects.get(title=title)

    @staticmethod
    def fetch_one_by_slug(slug):
        return Department.objects.get(slug=slug)


class KPIRepository:
    def __init__(self) -> None:
        self.department_repo = DepartmentRepository()

    def _fetch_all(self) -> QuerySet | List[KPIConfig]:
        return KPIConfig.objects.filter(is_active=True)

    def fetch_all_kpis_by_department(
        self, search_string: str, slug: bool = False
    ):
        if not search_string:
            raise NotTitleError
        department = None
        if slug:
            department = self.department_repo.fetch_one_by_slug(search_string)
        else:
            department = self.department_repo.fetch_one_by_title(search_string)
        return self._fetch_all().filter(department=department)

    def filter(self, **kwargs) -> QuerySet | List[KPIConfig]:
        return self.fetch_all_kpis_by_department.filter(**kwargs)

    def _fetch_kpi_value_by_phase_and_config(
        self, phase: KPIPhase, kpi: KPIConfig, is_glide=False
    ):
        try:
            return KPIValue.objects.get(kpi_phase=phase, kpi=kpi, is_glidepath=is_glide)
        except KPIValue.DoesNotExist:
            return None

    def generate_body_item(
        self, phase: KPIPhase, kpi: KPIConfig, is_glide=False
    ) -> MatrixValue:
        real_val = self._fetch_kpi_value_by_phase_and_config(phase=phase, kpi=kpi, is_glide=is_glide)
        return MatrixValue(kpi.id, phase.id, is_glide, real_val)

    def get_phases(self) -> QuerySet | List[KPIPhase]:
        return KPIPhase.objects.all()

    def fetch_one(self, title: str) -> KPIConfig:
        return KPIConfig.objects.get(title=title)

    