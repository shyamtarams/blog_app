# Generated by Django 2.2 on 2019-04-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog2', '0005_remove_blog2_usr_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog2',
            name='usr_id',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
