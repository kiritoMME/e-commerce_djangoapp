# Generated by Django 4.2.2 on 2023-06-17 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gallery_1',
            field=models.ImageField(default='static/images/product-null.jpg', upload_to='static/images/'),
        ),
    ]
