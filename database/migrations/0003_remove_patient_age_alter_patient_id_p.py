# Generated by Django 4.2.2 on 2023-06-11 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_availability_alter_patient_id_p_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_p',
            field=models.CharField(default='l7PP', max_length=4, primary_key=True, serialize=False),
        ),
    ]
