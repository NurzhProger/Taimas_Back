# Generated by Django 4.1.2 on 2023-01-26 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0022_organizations_checkedgps_alter_childs_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='childs',
            name='create_date',
            field=models.DateField(blank=None, default=datetime.datetime(2023, 1, 26, 16, 57, 30, 995301), null=None),
        ),
        migrations.AlterField(
            model_name='visits',
            name='create_date',
            field=models.DateTimeField(blank=None, default=datetime.datetime(2023, 1, 26, 16, 57, 31, 31301), null=None),
        ),
    ]
