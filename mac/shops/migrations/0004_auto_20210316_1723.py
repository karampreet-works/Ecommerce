# Generated by Django 3.1.7 on 2021-03-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0003_auto_20210316_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='desc',
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.CharField(default='', max_length=500),
        ),
    ]