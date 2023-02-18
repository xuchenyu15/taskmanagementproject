# Generated by Django 4.1.5 on 2023-02-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanagementapp', '0002_taskmanagementitem_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmanagementitem',
            name='content',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='taskmanagementitem',
            name='status',
            field=models.CharField(choices=[('Unfinished', 'Unfinished'), ('Finished', 'Finished'), ('In Progress', 'Inprogress'), ('At Rist', 'Atrist'), ('Planned', 'Planned'), ('Overdue', 'Overdue')], default='Unfinished', max_length=128),
        ),
    ]