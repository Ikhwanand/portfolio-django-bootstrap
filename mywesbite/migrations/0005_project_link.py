# Generated by Django 4.2.17 on 2024-12-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywesbite', '0004_alter_programmingskill_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
