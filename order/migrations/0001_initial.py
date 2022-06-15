# Generated by Django 4.0.4 on 2022-06-15 20:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='порядковый номер')),
                ('total_price', models.PositiveIntegerField(default=0, verbose_name='Всего')),
                ('price_with_discount', models.PositiveIntegerField(default=0, verbose_name='Итог')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Скидка')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='добавить время')),
                ('quantity_of_products', models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.shoppingcart')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиция заказа',
            },
        ),
    ]
