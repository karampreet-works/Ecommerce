# Generated by Django 3.1.7 on 2021-03-16 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0004_auto_20210316_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='description',
            new_name='desc',
        ),
    ]