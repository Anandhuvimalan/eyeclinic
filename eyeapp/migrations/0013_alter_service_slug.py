# Generated by Django 4.2.7 on 2023-12-02 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eyeapp', '0012_service_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]