# Generated by Django 2.0.5 on 2018-05-29 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0017_remove_organization_org_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='adviser_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organiation/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='aud_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g10_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g11_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g12_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g7_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g8_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='g9_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pio_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='pres_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='sec_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='tres_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='vp_picture',
            field=models.ImageField(blank=True, null=True, upload_to='organization/<django.db.models.fields.charfield>/profiles'),
        ),
    ]