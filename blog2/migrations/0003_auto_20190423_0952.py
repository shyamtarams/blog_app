# Generated by Django 2.2 on 2019-04-23 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0002_auto_20190423_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog2',
            old_name='user_rec',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='blog2',
            old_name='stripe_id',
            new_name='usr_id',
        ),
        migrations.RenameField(
            model_name='blog2',
            old_name='address_one',
            new_name='usr_nm',
        ),
        migrations.RemoveField(
            model_name='blog2',
            name='address_two',
        ),
        migrations.RemoveField(
            model_name='blog2',
            name='city',
        ),
        migrations.RemoveField(
            model_name='blog2',
            name='state',
        ),
    ]
