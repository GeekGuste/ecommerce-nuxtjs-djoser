# Generated by Django 4.0.1 on 2022-05-31 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_product_category_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='categories'),
        ),
    ]
