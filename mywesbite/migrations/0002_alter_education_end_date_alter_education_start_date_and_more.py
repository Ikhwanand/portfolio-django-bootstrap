# Generated by Django 4.2.17 on 2024-12-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywesbite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(),
        ),
    ]