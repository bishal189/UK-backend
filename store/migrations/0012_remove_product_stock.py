# Generated by Django 5.0.4 on 2024-05-08 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_merge_20240508_0611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stock',
        ),
    ]
