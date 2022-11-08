# Generated by Django 4.0.5 on 2022-11-05 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_resume1_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('message', models.TextField(max_length=400)),
            ],
        ),
    ]
