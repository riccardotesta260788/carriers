# Generated by Django 2.0 on 2018-11-14 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastweb', '0002_auto_20181114_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='id',
            field=models.BigIntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
