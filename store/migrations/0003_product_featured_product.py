# Generated by Django 4.2.2 on 2023-06-10 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_rate_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='featured_product',
            field=models.BooleanField(default=False),
        ),
    ]
