# Generated by Django 3.1.3 on 2021-02-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0004_auto_20210221_0928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diarydetail',
            name='img',
            field=models.ImageField(default='None', upload_to=''),
        ),
    ]
