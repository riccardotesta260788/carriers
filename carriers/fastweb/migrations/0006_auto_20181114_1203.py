# Generated by Django 2.0 on 2018-11-14 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fastweb', '0005_auto_20181114_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offers',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='userinteraction',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]