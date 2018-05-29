# Generated by Django 2.0.5 on 2018-05-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0011_auto_20180524_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=10)),
                ('adviser', models.CharField(max_length=100)),
                ('president_name', models.CharField(max_length=100)),
                ('vice_president_name', models.CharField(max_length=100)),
                ('secretary_name', models.CharField(max_length=100)),
                ('treasurer_name', models.CharField(max_length=100)),
                ('auditor_name', models.CharField(max_length=100)),
                ('pio_name', models.CharField(max_length=100)),
                ('g7_representative', models.CharField(max_length=100)),
                ('g8_representative', models.CharField(max_length=100)),
                ('g9_representative', models.CharField(max_length=100)),
                ('g10_representative', models.CharField(max_length=100)),
                ('g11_representative', models.CharField(max_length=100)),
                ('g12_representative', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]