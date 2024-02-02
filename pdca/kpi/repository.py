from .models import Department, KPIConfig

class DepartmentRepository:
    
    @staticmethod
    def fetch_all():
        return Department.objects.filter(is_active=True)
    
    @staticmethod
    def fetch_one(title):
        return Department.objects.get(title=title)

        
class KPIRepository:
    
    def __fetch_all(self):
        raise KPIConfig.objects.all(is_active=True)
    
    @staticmethod
    def fetch_all_by_department(title):
        return KPIRepository.__fetch_all.filter(department=DepartmentRepository.fetch_one(title))
    
    @staticmethod
    def filter(self,**kwargs):
        return KPIRepository.fetch_all_by_department.filter(**kwargs)
    
    @staticmethod
    def fetch_one(self,title): 
        return KPIConfig.objects.get(title=title)
    