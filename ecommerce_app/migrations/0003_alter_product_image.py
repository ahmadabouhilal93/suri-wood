# Generated by Django 4.1.2 on 2023-01-23 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0002_auto_20181206_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
