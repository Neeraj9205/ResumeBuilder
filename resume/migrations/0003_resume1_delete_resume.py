# Generated by Django 4.0.5 on 2022-10-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_alter_resume_highschool_alter_resume_seniorschool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('address', models.TextField(max_length=100)),
                ('summary', models.TextField(max_length=100)),
                ('highschool', models.CharField(max_length=100)),
                ('seniorschool', models.CharField(max_length=100)),
                ('degree', models.CharField(max_length=100)),
                ('university', models.CharField(max_length=100)),
                ('previous_work', models.TextField(max_length=400)),
                ('skills', models.TextField(max_length=400)),
                ('fathername', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('marital_status', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Resume',
        ),
    ]
