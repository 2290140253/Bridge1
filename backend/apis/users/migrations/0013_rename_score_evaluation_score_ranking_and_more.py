# Generated by Django 5.0.7 on 2024-11-27 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_evaluation_weight_evaluation_weight_ranking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='evaluation',
            old_name='score',
            new_name='score_ranking',
        ),
        migrations.RenameField(
            model_name='evaluation',
            old_name='weight_ranking',
            new_name='weight',
        ),
    ]
