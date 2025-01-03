# Generated by Django 5.1.2 on 2024-10-22 16:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='maps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('scheme', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='workplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_code', models.CharField(max_length=10)),
                ('equipment', models.TextField()),
                ('map_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workplace_map', to='booking.maps')),
            ],
        ),
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_workplace', to=settings.AUTH_USER_MODEL)),
                ('workplace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booked_workplace', to='booking.workplace')),
            ],
        ),
    ]
