# Generated by Django 4.2.17 on 2024-12-16 16:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywesbite', '0002_alter_education_end_date_alter_education_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmingskill',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/', validators=[django.core.validators.FileExtensionValidator(['svg'])]),
        ),
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='projects/', validators=[django.core.validators.FileExtensionValidator(['jpg', 'jpeg', 'png'])]),
        ),
    ]
