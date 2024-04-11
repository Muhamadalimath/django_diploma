# Generated by Django 4.2.6 on 2023-11-18 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_image_category_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('title',)},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='created',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='free_delivery_status',
            new_name='freeDelivery',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]