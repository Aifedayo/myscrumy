# Generated by Django 2.0.4 on 2018-04-27 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lagscrumy', '0008_auto_20180427_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='goalstatus',
            name='goals',
            field=models.CharField(choices=[('WG', 'Weekly Goals'), ('DT', 'Daily Task')], default='DT', max_length=50, null=True),
        ),
    ]
