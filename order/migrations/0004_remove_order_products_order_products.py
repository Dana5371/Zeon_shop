# Generated by Django 4.0.4 on 2022-06-16 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0003_alter_order_city_alter_order_country_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='cart.shoppingcart'),
        ),
    ]