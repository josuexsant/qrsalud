# Generated by Django 4.1.1 on 2022-10-04 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr_app', '0007_report_blood_alter_report_age_alter_report_email_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='diabetes',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Diabetes'),
        ),
        migrations.AddField(
            model_name='report',
            name='extra_info',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Información importante que desea agregar'),
        ),
        migrations.AddField(
            model_name='report',
            name='med_1',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Medicamento 1'),
        ),
        migrations.AddField(
            model_name='report',
            name='med_2',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Medicamento 2'),
        ),
        migrations.AddField(
            model_name='report',
            name='med_3',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Medicamento 3'),
        ),
        migrations.AddField(
            model_name='report',
            name='med_4',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Medicamento 4'),
        ),
    ]
