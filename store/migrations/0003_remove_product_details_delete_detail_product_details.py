# Generated by Django 5.0.4 on 2024-05-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_detail_alter_product_price_product_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='details',
        ),
        migrations.DeleteModel(
            name='Detail',
        ),
        migrations.AddField(
            model_name='product',
            name='details',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]