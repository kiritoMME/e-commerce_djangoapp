# Generated by Django 4.2.2 on 2023-06-15 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_order_is_delivered_alter_order_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='user',
        ),
    ]