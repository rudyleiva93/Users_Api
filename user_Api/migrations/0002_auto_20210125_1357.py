# Generated by Django 3.1.4 on 2021-01-25 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]