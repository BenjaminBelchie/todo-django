# Generated by Django 3.1.4 on 2021-03-30 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210329_1542'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='item',
            new_name='items',
        ),
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]
