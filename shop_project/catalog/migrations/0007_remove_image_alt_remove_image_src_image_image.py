# Generated by Django 4.2.6 on 2023-11-25 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_product_images_product_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='alt',
        ),
        migrations.RemoveField(
            model_name='image',
            name='src',
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(default='D:/skillbox/shop_project/frontend/static/frontend/assets/img/content/home/bigGoods.png', upload_to='images'),
        ),
    ]
