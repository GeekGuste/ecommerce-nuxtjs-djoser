# Generated by Django 4.0.1 on 2022-05-15 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_order_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='dfv', max_length=100),
            preserve_default=False,
        ),
    ]
