# Generated by Django 4.1.6 on 2023-03-08 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_alter_products_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]