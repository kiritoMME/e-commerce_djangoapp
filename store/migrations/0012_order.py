# Generated by Django 4.2.2 on 2023-06-11 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_rename_image_2_product_gallery_1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500)),
                ('product', models.CharField(max_length=500)),
                ('count', models.IntegerField()),
            ],
        ),
    ]
