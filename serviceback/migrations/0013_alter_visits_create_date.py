# Generated by Django 4.1.2 on 2023-01-20 09:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0012_groups_create_date_organizations_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visits',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 20, 14, 46, 34, 689204), null=True),
        ),
    ]
