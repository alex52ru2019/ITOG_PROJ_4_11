# Generated by Django 5.1.2 on 2024-11-09 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_rename_shopping2_shopping_now'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping_now',
            new_name='Shopping',
        ),
    ]
