# Generated by Django 5.1.2 on 2024-11-09 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_select_shop_delete_shopping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='select_shop',
            name='created_at',
        ),
    ]