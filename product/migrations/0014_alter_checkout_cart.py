# Generated by Django 5.0.6 on 2024-07-02 06:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.cartitem'),
        ),
    ]
