# Generated by Django 2.1.1 on 2018-09-18 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlquery', '0002_auto_20180917_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysqlquerylog',
            name='host',
            field=models.CharField(max_length=128, verbose_name='目标数据库地址'),
        ),
    ]
