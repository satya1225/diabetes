# Generated by Django 3.0.4 on 2020-03-19 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eradicate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='date_of_birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='diabetes_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='heartdiease_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='hypertension_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='kidney_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='liverdisease_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='obesity_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='pcod_long',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='thyroid_long',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
