# Generated by Django 5.0.6 on 2024-07-02 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_checkout_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='narxi',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
