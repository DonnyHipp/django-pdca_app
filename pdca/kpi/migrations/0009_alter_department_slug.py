# Generated by Django 5.0.1 on 2024-02-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0008_alter_category_title_alter_department_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='afd', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
