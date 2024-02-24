# from typing import List

# from django.db.models import QuerySet

# from .schemas import MatrixValue

# from .exceptions import NotTitleError
# from .models import Department, KPIConfig, KPIPhase, KPIValue

from abc import ABC, abstractmethod
from typing import List, Optional
from django.db.models import QuerySet

from .models import Department, KPIConfig, KPIPhase, KPIValue


class DepartmentRepositoryInterface(ABC):
    @abstractmethod
    def fetch_all(self) -> List[Department]:
        raise NotImplementedError

    @abstractmethod
    def fetch_one(self):
        raise NotImplementedError

    @abstractmethod
    def fetch_by_title(self, title: str) -> Optional[Department]:
        raise NotImplementedError

    @abstractmethod
    def fetch_by_slug(self, slug: str) -> Optional[Department]:
        raise NotImplementedError

    @abstractmethod
    def create(self, title: str) -> Department:
        raise NotImplementedError

    @abstractmethod
    def update(self, department: Department) -> Department:
        raise NotImplementedError

    @abstractmethod
    def delete(self, department: Department) -> None:
        raise NotImplementedError


class DepartmentRepository(DepartmentRepositoryInterface):
    def fetch_all() -> QuerySet[Department]:
        return Department.objects.filter(is_active=True)

    def fetch_one(self, search_string, is_slug=False):
        if is_slug:
            return self._fetch_by_slug(search_string)
        else:
            return self._fetch_by_title(search_string)

    def _fetch_by_title(self, title: str) -> Optional[Department]:
        return Department.objects.get(title=title)

    def _fetch_by_slug(self, slug: str) -> Optional[Department]:
        return Department.objects.get(slug=slug)

    def create(self, title: str) -> Department:
        return Department.objects.create(title=title)

    def update(self, department: Department) -> Department:
        department.objects.update()
        return department

    def delete(self, department: Department) -> None:
        department.delete()


class KPIRepositoryInterface(ABC):
    def fetch_all(self) -> QuerySet[KPIConfig]:
        raise NotImplementedError

    def filter(self, **kwargs) -> QuerySet[KPIConfig]:
        raise NotImplementedError

    def get_phases(self) -> QuerySet[KPIPhase]:
        raise NotImplementedError

    def get_all_real_kpi(self, is_glidepath: bool) -> QuerySet[KPIPhase]:
        raise NotImplementedError

    def fetch_one(self, title: str) -> KPIConfig:
        raise NotImplementedError


class KPIRepository(KPIRepositoryInterface):
    def fetch_all(self) -> QuerySet[KPIConfig]:
        return KPIConfig.objects.filter(is_active=True)

    def filter(self, **kwargs) -> QuerySet[KPIConfig]:
        return self._fetch_all().filter(**kwargs)

    def get_all_real_kpi(self, is_glidepath=False) -> QuerySet[KPIPhase]:
        return KPIValue.objects.filter(is_glidepath=is_glidepath)

    def get_phases(self) -> QuerySet[KPIPhase]:
        return KPIPhase.objects.all()

    def fetch_one(self, title: str) -> KPIConfig:
        return KPIConfig.objects.get(title=title)
