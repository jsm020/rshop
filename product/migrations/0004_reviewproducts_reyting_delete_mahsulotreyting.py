# Generated by Django 5.0.6 on 2024-06-27 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_reviewproducts_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewproducts',
            name='reyting',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='mahsulotReyting',
        ),
    ]