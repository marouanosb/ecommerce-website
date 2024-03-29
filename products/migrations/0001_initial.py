# Generated by Django 5.0 on 2024-01-09 16:08

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
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('FOOD', 'Nourriture'), ('COSMETIC', 'Cosmetique'), ('ELECTRONIC', 'Electronique'), ('CLOTHS', 'Vetements')], max_length=10)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=20)),
                ('reviews', models.IntegerField()),
                ('reviews_number', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('vendor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
