# Generated by Django 5.0.7 on 2024-11-25 10:34

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('cycle_id', models.CharField(max_length=60, primary_key=True, serialize=False, verbose_name='周期编号')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
                ('cycle_number', models.IntegerField(verbose_name='周期数字')),
                ('has_decided', models.BooleanField(default=False, verbose_name='是否已决策')),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('round_id', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='轮次编号')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='开始时间')),
                ('end_time', models.DateTimeField(blank=True, null=True, verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('student_id', models.CharField(max_length=20, unique=True, verbose_name='学号')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('name', models.CharField(max_length=50, verbose_name='学生姓名')),
                ('user_class', models.CharField(max_length=50, verbose_name='班级')),
                ('team_name', models.CharField(max_length=50, verbose_name='队名')),
                ('phone', models.CharField(max_length=15, verbose_name='电话')),
                ('group', models.IntegerField(verbose_name='组号')),
                ('number', models.IntegerField(verbose_name='企业编号')),
                ('register_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('rest_rounds', models.IntegerField(blank=True, null=True, verbose_name='剩余重开机会')),
            ],
        ),
        migrations.CreateModel(
            name='MarketReport',
            fields=[
                ('market_report_id', models.AutoField(primary_key=True, serialize=False, verbose_name='报告编号')),
                ('market_capacity', models.CharField(max_length=255, verbose_name='市场容量')),
                ('raw_materials', models.CharField(max_length=255, verbose_name='原材料')),
                ('attachments', models.CharField(max_length=255, verbose_name='附件')),
                ('personnel_costs', models.CharField(max_length=255, verbose_name='人员费用')),
                ('bulk_tendering', models.CharField(max_length=255, verbose_name='批量招标')),
                ('bulk_ordering', models.CharField(max_length=255, verbose_name='批量订购')),
                ('ordering_price', models.CharField(max_length=255, verbose_name='订购价格')),
                ('cycle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cycle', verbose_name='周期编号')),
            ],
        ),
        migrations.AddField(
            model_name='cycle',
            name='round_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.round', verbose_name='轮次编号'),
        ),
        migrations.AddField(
            model_name='round',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='用户编号'),
        ),
        migrations.AddField(
            model_name='cycle',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user', verbose_name='用户编号'),
        ),
    ]
