# Generated by Django 4.0.10 on 2023-11-26 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_product_best_before_product_valid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='best_before',
            field=models.DateField(),
        ),
    ]