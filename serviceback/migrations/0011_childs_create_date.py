# Generated by Django 4.1.2 on 2023-01-20 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceback', '0010_childs_birthday_childs_gernder'),
    ]

    operations = [
        migrations.AddField(
            model_name='childs',
            name='create_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
