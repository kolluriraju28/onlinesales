# Generated by Django 2.2.1 on 2019-06-07 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_agent', '0005_soldproperty_client_uname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldproperty',
            name='date_of_sold',
            field=models.DateField(auto_now_add=True),
        ),
    ]
