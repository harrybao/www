# Generated by Django 2.0 on 2018-04-24 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20180423_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='readRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_id', models.CharField(max_length=200, null=True, verbose_name='阅读用户')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Article')),
            ],
            options={
                'verbose_name': '文章浏览记录',
                'verbose_name_plural': '文章浏览记录',
            },
        ),
    ]
