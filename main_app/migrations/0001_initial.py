# Generated by Django 3.2.3 on 2021-05-14 04:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mineral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('m_class', models.CharField(max_length=100)),
                ('colour', models.CharField(max_length=100)),
                ('hardness', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)])),
                ('magnetic', models.BooleanField(default=False)),
            ],
        ),
    ]
