# Generated by Django 4.2.2 on 2023-06-11 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_offer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('comment', models.CharField(default='this is from django default comment elit. Quis, repellat. Id natus aut, quasi unde voluptatum, ipsa fugit esse enim numquam officiis cupiditate repellendus nihil fuga. A iure fugit hic. lo', max_length=1000000)),
                ('rate_text', models.CharField(default='FFFFF', max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]