# Generated by Django 4.1.2 on 2023-01-20 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0017_alter_visits_create_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='childs',
            old_name='gernder',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='visits',
            name='create_date',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2023, 1, 21, 0, 5, 17, 235485), null=None),
        ),
    ]
