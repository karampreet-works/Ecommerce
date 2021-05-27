# Generated by Django 3.1.7 on 2021-03-21 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0006_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='updateOrder',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default='')),
                ('update_desc', models.CharField(max_length=500)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
