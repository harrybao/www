# Generated by Django 2.0 on 2018-04-24 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_readrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professional',
            name='direction',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='就业前景'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='main_class',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='学科'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='objective',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='培养目标'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='practice',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='学习课程'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='profes_name',
            field=models.CharField(max_length=400, verbose_name='专业名称'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='profess_class',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='专业类别'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='related',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='专业介绍'),
        ),
        migrations.AlterField(
            model_name='professional',
            name='tra_require',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='培养要求'),
        ),
    ]