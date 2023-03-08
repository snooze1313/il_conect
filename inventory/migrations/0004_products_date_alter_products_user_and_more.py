# Generated by Django 4.1.6 on 2023-03-08 00:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventory', '0003_products_description_supplier_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='country',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='maincontact',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]