# Generated by Django 4.1.2 on 2022-10-24 22:42

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to=app.models.ProductImageUploadHandler),
        ),
    ]