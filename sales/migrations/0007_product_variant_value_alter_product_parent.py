# Generated by Django 4.0.1 on 2022-03-24 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0006_product_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='variant_value',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='sales.product'),
        ),
    ]