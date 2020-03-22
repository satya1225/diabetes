# Generated by Django 3.0.4 on 2020-03-19 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eradicate', '0002_auto_20200318_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthist',
            name='diabetes',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Diabetes?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='heartdiease',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Heart desease?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='hypertension',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Hypertension?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='kidney',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Kidney desease?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='liverdisease',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Liver desease?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='obesity',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Are you obese?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='pcod',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with PCOD/PCOS (Females Only)?'),
        ),
        migrations.AlterField(
            model_name='patienthist',
            name='thyroid',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='Have you ever been diagnosed with Thyroid problems?'),
        ),
    ]