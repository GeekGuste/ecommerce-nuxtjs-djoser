# Generated by Django 4.0.1 on 2022-03-23 22:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_alter_product_promo_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_variant',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='variant_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sales.varianttype'),
        ),
    ]