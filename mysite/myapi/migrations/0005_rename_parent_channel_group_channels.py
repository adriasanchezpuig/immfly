# Generated by Django 4.1.4 on 2022-12-16 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0004_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='parent_channel',
            new_name='channels',
        ),
    ]
