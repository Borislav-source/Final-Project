# Generated by Django 3.2.6 on 2021-08-06 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EngineModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('image', models.FileField(upload_to='media/Manufacturers')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('image_url', models.URLField()),
                ('production_date', models.DateTimeField()),
                ('engine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.enginemodel')),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(choices=[('Car', 'Car'), ('Truck', 'Truck'), ('Motorcycle', 'Motorcycle')], max_length=25)),
                ('manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.manufacturer')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehiclemodels')),
            ],
        ),
    ]
