# Generated by Django 2.0 on 2018-04-21 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180420_2048'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='question',
            field=models.CharField(max_length=200, null=True, verbose_name='问题编号'),
        ),
    ]
