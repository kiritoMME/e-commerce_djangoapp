# Generated by Django 4.2.2 on 2023-06-11 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_image_2_product_image_3_product_image_4'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_2',
            new_name='gallery_1',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_3',
            new_name='gallery_2',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='image_4',
            new_name='gallery_3',
        ),
        migrations.AddField(
            model_name='product',
            name='gallery_4',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/'),
        ),
    ]
