# Generated by Django 5.0.7 on 2024-11-27 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_remove_evaluationweight_round_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('evaluation_id', models.AutoField(primary_key=True, serialize=False)),
                ('project', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('cycle_number', models.IntegerField()),
                ('weight', models.FloatField()),
                ('value', models.FloatField()),
                ('score', models.FloatField()),
                ('round_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.round')),
            ],
            options={
                'verbose_name': 'Evaluation',
                'verbose_name_plural': 'Evaluations',
                'db_table': 'evaluation',
            },
        ),
    ]
