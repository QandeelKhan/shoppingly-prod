# Generated by Django 3.1.7 on 2021-02-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210224_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Diliverd', 'Diliverd'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]
