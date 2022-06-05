# Generated by Django 4.0.1 on 2022-05-31 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_category_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='sales.Category'),
        ),
    ]