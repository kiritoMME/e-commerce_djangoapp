# Generated by Django 4.2.2 on 2023-06-16 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_confirmed_orders_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='is_delivered',
        ),
    ]