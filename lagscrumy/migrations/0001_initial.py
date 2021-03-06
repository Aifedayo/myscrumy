# Generated by Django 2.0.4 on 2018-04-25 20:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('WG', 'Weekly Goals'), ('DT', 'Daily Task'), ('P', 'Pending'), ('V', 'Verified')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyGoals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=django.utils.timezone.now, max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField()),
                ('goalstatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lagscrumy.GoalStatus')),
            ],
        ),
        migrations.CreateModel(
            name='ScrumyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('username', models.EmailField(max_length=300)),
            ],
        ),
        migrations.AddField(
            model_name='scrumygoals',
            name='scrumyuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lagscrumy.ScrumyUser'),
        ),
        migrations.AddField(
            model_name='goalstatus',
            name='role',
            field=models.ManyToManyField(through='lagscrumy.ScrumyGoals', to='lagscrumy.ScrumyUser'),
        ),
    ]
