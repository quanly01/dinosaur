# Generated by Django 3.0.3 on 2022-11-01 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20221101_1012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagories',
            new_name='Toppings',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='catagories',
            new_name='toppings',
        ),
    ]
