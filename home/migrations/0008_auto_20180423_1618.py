# Generated by Django 2.0 on 2018-04-23 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20180423_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='context',
            field=models.TextField(verbose_name='文章内容'),
        ),
    ]
