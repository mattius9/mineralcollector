# Generated by Django 3.2.3 on 2021-05-18 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_viewing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='viewing',
            old_name='security_level',
            new_name='level',
        ),
        migrations.AlterField(
            model_name='viewing',
            name='date',
            field=models.DateField(verbose_name='viewing date'),
        ),
    ]
