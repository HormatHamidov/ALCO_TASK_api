# Generated by Django 4.1 on 2022-08-30 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_task_slug_alter_task_qaralama'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='slug',
        ),
    ]
