# Generated by Django 4.0.1 on 2022-05-15 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0005_order_delivery_charges'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderProducts', to='sales.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product')),
            ],
        ),
    ]
