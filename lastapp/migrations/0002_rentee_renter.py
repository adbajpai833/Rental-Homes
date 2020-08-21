# Generated by Django 2.2.3 on 2020-05-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lastapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rentee',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('maritial_status', models.CharField(max_length=50)),
                ('family_member', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='renter',
            fields=[
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=15)),
                ('mobile_number', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=15)),
                ('locality', models.CharField(max_length=20)),
                ('house_number', models.CharField(max_length=10)),
                ('landmark', models.CharField(max_length=20)),
                ('no_of_rooms', models.CharField(max_length=5)),
                ('kitchen', models.CharField(max_length=5)),
                ('bathroom', models.CharField(max_length=5)),
                ('location', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=50)),
                ('electricity_charge', models.CharField(max_length=50)),
                ('water_charge', models.CharField(max_length=50)),
                ('rent_value', models.CharField(max_length=50)),
            ],
        ),
    ]