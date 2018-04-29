# Generated by Django 2.0.4 on 2018-04-27 22:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lagscrumy', '0009_goalstatus_goals'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalstatus',
            name='verified_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='goalstatus',
            name='completed_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]