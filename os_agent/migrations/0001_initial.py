# Generated by Django 2.2.1 on 2019-06-06 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('os_client', '0001_initial'),
        ('os_admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('p_no', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('photo', models.ImageField(upload_to='Property/')),
                ('size', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=30)),
                ('facing', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=30)),
                ('comment', models.CharField(max_length=30)),
                ('add_date', models.DateField()),
                ('sold_date', models.DateField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_admin.Agent')),
            ],
        ),
        migrations.CreateModel(
            name='Soldproperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_sold', models.DateField()),
                ('p_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_agent.Property')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyBlocked',
            fields=[
                ('bno', models.AutoField(primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('client_uname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_client.Client')),
                ('p_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='os_agent.Property')),
            ],
        ),
    ]
