# Generated by Django 4.1.5 on 2023-02-18 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagementapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmanagementitem',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taskmanagementitem',
            name='status',
            field=models.CharField(choices=[('U', 'Unfinished'), ('F', 'Finished'), ('I', 'In Progress'), ('A', 'At Rist'), ('P', 'Planned'), ('O', 'Overdue')], default='U', max_length=1),
        ),
    ]
