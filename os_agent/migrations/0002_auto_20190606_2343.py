# Generated by Django 2.2.1 on 2019-06-06 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('os_agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='add_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='sold_date',
            field=models.DateField(default=True),
        ),
    ]
