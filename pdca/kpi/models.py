from colorfield.fields import ColorField

from django.db import models
from slugify import slugify


class BaseContent(models.Model):
    title = models.CharField(max_length=255, verbose_name="Наименование", unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)

    class Meta:
        abstract = True


class Department(BaseContent):
    COLOR_PALETTE = [
        (
            "#FFFFFF",
            "white",
        ),
        (
            "#000000",
            "black",
        ),
    ]
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    is_active = models.BooleanField(default=True, verbose_name="Активный статус")
    text_color = models.CharField(
        choices=COLOR_PALETTE, default="#000000", max_length=7
    )
    back_color = ColorField(format="hexa", blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Entity(BaseContent):
    pass


class Category(BaseContent):
    pass


class KPIPhase(BaseContent):
    is_active = models.BooleanField(default=True, verbose_name="Активный статус")


class KPI(models.Model):
    title = models.TextField(max_length=500, verbose_name="Наименование", unique=True)
    is_percentage = models.BooleanField(
        default=False, verbose_name="Процентная метрика"
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.title)


class KPIConfig(models.Model):
    kpi = models.ForeignKey(KPI, on_delete=models.DO_NOTHING, verbose_name="KPI")
    department = models.ForeignKey(
        Department, on_delete=models.DO_NOTHING, verbose_name="Отдел"
    )
    entity = models.ForeignKey(
        Entity,
        on_delete=models.DO_NOTHING,
        blank=True,
        verbose_name="Производственный участок",
    )
    category = models.ForeignKey(
        Category, on_delete=models.DO_NOTHING, blank=True, verbose_name="Категория"
    )
    is_active = models.BooleanField(default=True, verbose_name="Активный статус")

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{str(self.kpi.title)} - {str(self.department)}"


class KPIPhase(BaseContent):  # noqa: F811
    is_active = models.BooleanField(default=True, verbose_name="Активный статус")


class KPIValue(models.Model):
    years_list = (
        ("2021", "2021"),
        ("2022", "2022"),
        ("2023", "2023"),
        ("2024", "2024"),
        ("2025", "2025"),
        ("2026", "2026"),
    )
    kpi = models.ForeignKey(KPIConfig, on_delete=models.DO_NOTHING, verbose_name="KPI")
    kpi_phase = models.ForeignKey(
        KPIPhase, on_delete=models.DO_NOTHING, verbose_name="Период"
    )
    is_glidepath = models.BooleanField(default=False, verbose_name="Таргет")
    year = models.CharField(choices=years_list, default="2024", max_length=4)
    value = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Значение")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{str(self.kpi.__str__())} - {"Glide" if self.is_glidepath else "Real"} - {str(self.year)}'

    class Meta:
        unique_together = ["year", "is_glidepath", "kpi_phase", "kpi"]


