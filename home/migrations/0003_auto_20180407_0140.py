# Generated by Django 2.0 on 2018-04-07 01:40

from django.db import migrations, models
import django.db.models.deletion
import system.storage


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180405_0801'),
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('College_name', models.CharField(max_length=200, verbose_name='学院名称')),
            ],
        ),
        migrations.CreateModel(
            name='fare_line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_batch', models.CharField(max_length=50, verbose_name='批次')),
                ('fare_science', models.CharField(max_length=20, verbose_name='理科')),
                ('fare_arts', models.CharField(max_length=20, verbose_name='文科')),
            ],
        ),
        migrations.CreateModel(
            name='Over_year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=100, verbose_name='批次')),
                ('dics', models.CharField(max_length=100, verbose_name='科类')),
                ('major', models.CharField(max_length=200, verbose_name='专业')),
                ('control_line', models.CharField(max_length=50, verbose_name='控制线')),
                ('enrolment', models.CharField(max_length=50, verbose_name='录取人数')),
                ('highest_score', models.CharField(max_length=50, verbose_name='最高分')),
                ('minimum_score', models.CharField(max_length=50, verbose_name='最低分')),
                ('average_score', models.CharField(max_length=50, verbose_name='平均分')),
            ],
        ),
        migrations.CreateModel(
            name='que_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', models.CharField(max_length=200, verbose_name='回复者')),
                ('ans_time', models.DateField(verbose_name='回复时间')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_tittle', models.CharField(max_length=100, verbose_name='标题')),
                ('que_text', models.CharField(max_length=400, verbose_name='问题')),
                ('que_image', models.ImageField(storage=system.storage.ImageStorage(), upload_to='./quetion', verbose_name='图片')),
                ('questioner', models.CharField(max_length=200, verbose_name='提问者')),
                ('que_time', models.DateField(verbose_name='提问时间')),
                ('que_view', models.CharField(max_length=20, verbose_name='查看次数')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='学校编号')),
                ('school_name', models.CharField(max_length=100, verbose_name='学校名称')),
                ('school_badge', models.ImageField(storage=system.storage.ImageStorage(), upload_to='./badge/', verbose_name='校徽')),
                ('school_motto', models.CharField(max_length=60, verbose_name='校训')),
            ],
        ),
        migrations.CreateModel(
            name='school_add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_name', models.CharField(max_length=300, verbose_name='地址')),
                ('address_gps', models.CharField(max_length=50, verbose_name='经度')),
                ('address_gpss', models.CharField(max_length=50, verbose_name='纬度')),
            ],
        ),
        migrations.CreateModel(
            name='School_Img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_ph', models.ImageField(storage=system.storage.ImageStorage(), upload_to='./image/', verbose_name='学校图片')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School')),
            ],
        ),
        migrations.AddField(
            model_name='que_answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Questions'),
        ),
        migrations.AddField(
            model_name='college',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.School'),
        ),
    ]