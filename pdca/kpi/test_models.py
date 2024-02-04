from django.test import TestCase
from .models import Department, Entity, Category


class ModelTestCase(TestCase):
    def setUp(self):
        # Создание тестовых данных для использования в тестах
        self.department = Department.objects.create(title="Test Department")
        self.entity = Entity.objects.create(title="Test Entity")
        self.category = Category.objects.create(title="Test Category")

    def test_department_creation(self):
        department = Department.objects.get(title="Test Department")

        self.assertEqual(str(department), "Test Department")
        self.assertEqual(department.slug, "test-department")
        self.assertTrue(department.is_active)
        self.assertIsNotNone(department.slug)
