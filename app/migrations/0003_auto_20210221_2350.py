# Generated by Django 3.1.7 on 2021-02-21 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210221_2147'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discount_price',
            new_name='discounted_price',
        ),
    ]
