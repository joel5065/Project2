# Generated by Django 4.0.5 on 2022-07-08 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('OPS', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aeronefs',
            new_name='Aeronef',
        ),
        migrations.RenameModel(
            old_name='Cellules',
            new_name='Cellule',
        ),
    ]
