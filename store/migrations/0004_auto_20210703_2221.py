# Generated by Django 3.0.4 on 2021-07-03 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20210630_2108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address',
            new_name='block',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='floor',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='state',
            new_name='hostel',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='zipcode',
            new_name='roomno',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
