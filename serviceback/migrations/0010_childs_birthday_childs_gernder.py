# Generated by Django 4.1.2 on 2023-01-20 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0009_childs_is_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='childs',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='childs',
            name='gernder',
            field=models.TextField(blank=True, null=True),
        ),
    ]
