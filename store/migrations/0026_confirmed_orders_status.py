# Generated by Django 4.2.2 on 2023-06-16 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_remove_confirmed_orders_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmed_orders',
            name='status',
            field=models.CharField(default='none', max_length=20),
        ),
    ]
