# Generated by Django 3.2.8 on 2021-10-15 13:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='Lessons',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 18, 5, 50, 301729), verbose_name='Registratsiya sanasi:'),
        ),
    ]