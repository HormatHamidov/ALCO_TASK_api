# Generated by Django 4.1 on 2022-08-30 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_task_bank_account_alter_task_city_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='qaralama',
        ),
    ]