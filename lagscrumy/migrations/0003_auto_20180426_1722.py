# Generated by Django 2.0.4 on 2018-04-26 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lagscrumy', '0002_auto_20180426_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrumygoals',
            name='scrumyuser_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='lagscrumy.ScrumyUser'),
        ),
    ]