# Generated by Django 2.0 on 2018-11-14 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastweb', '0004_auto_20181114_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
