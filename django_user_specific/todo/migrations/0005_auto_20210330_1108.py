# Generated by Django 3.1.4 on 2021-03-30 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210330_1104'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='items',
            new_name='Item',
        ),
    ]
