# Generated by Django 4.1.2 on 2023-01-26 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0024_remove_visits_create_date_alter_childs_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='visits',
            name='create_date',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2023, 1, 26, 17, 37, 20, 671555), null=None),
        ),
        migrations.AlterField(
            model_name='childs',
            name='create_date',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 1, 26, 17, 37, 20, 640312), null=None),
        ),
    ]