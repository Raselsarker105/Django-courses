# Generated by Django 5.0 on 2024-01-20 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_contactmodel_user'),
        ('projects', '0003_projectmodel_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ratingmodel',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projectmodel'),
        ),
        migrations.AddField(
            model_name='ratingmodel',
            name='average_rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
