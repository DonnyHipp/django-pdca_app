from typing import List

from django.core.exceptions import ObjectDoesNotExist
from django.db.models import QuerySet
from .models import  KPIConfig

from .repository import DepartmentRepository, KPIRepository

__all__ = [
    'DepartmentService', 'KPIservice'
]

class DepartmentService:
    
    def __init__(self,repository) -> None:
        self.repository = repository
    
    def fetch_all(self):
        try:
            return self.repository.fetch_all()
        except ObjectDoesNotExist:
            return None
        

    def fetch_one(self):
        try:
            return self.repository.fetch_one()
        except ObjectDoesNotExist:
            return None

        
class KPIservice:
    
    def __init__(self,repository) -> None:
        self.repository = repository
        
    def get_kpi_list(self,department_title:str) -> QuerySet | List[KPIConfig]:
        try:
            return self.repository.fetch_all_by_department(department_title)
        except ObjectDoesNotExist:
            return None