# Generated by Django 4.2.2 on 2023-06-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_patient_age_alter_patient_id_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='id_p',
            field=models.CharField(default='Sd0a', max_length=4, primary_key=True, serialize=False),
        ),
    ]
