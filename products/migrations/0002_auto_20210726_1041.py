# Generated by Django 2.2.18 on 2021-07-26 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'Категория товаров', 'verbose_name_plural': 'Категории товаров'},
        ),
    ]
