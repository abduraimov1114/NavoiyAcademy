# Generated by Django 3.2.8 on 2021-10-15 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0006_alter_lessons_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 15, 18, 7, 40, 669969), verbose_name='Registratsiya sanasi:'),
        ),
    ]
