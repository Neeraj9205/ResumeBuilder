# Generated by Django 4.0.5 on 2022-10-19 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='highschool',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='resume',
            name='seniorschool',
            field=models.CharField(max_length=100),
        ),
    ]
