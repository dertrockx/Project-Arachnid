# Generated by Django 2.0.5 on 2018-06-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0038_auto_20180604_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='opening',
            field=models.CharField(max_length=10000),
        ),
    ]