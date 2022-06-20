# Generated by Django 4.0.4 on 2022-06-20 10:18

import datetime
import django.core.validators
from django.db import migrations, models


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
                ('name', models.CharField(max_length=155, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=155, verbose_name='Фамилия')),
                ('number_of_phone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(regex='^\\+?1?\\d{8,15}$')], verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=200, verbose_name='Страна')),
                ('city', models.CharField(max_length=155, verbose_name='Город')),
                ('status_of_order', models.CharField(choices=[('new', 'Новый'), ('issued', 'Оформлен'), ('cancelled', 'Отменен')], default='new', max_length=155, verbose_name='Статус заказа')),
                ('order_sn', models.CharField(blank=True, max_length=30, null=True, unique=True, verbose_name='порядковый номер')),
                ('total_price', models.PositiveIntegerField(default=0, verbose_name='Всего')),
                ('price_with_discount', models.PositiveIntegerField(default=0, verbose_name='Итог')),
                ('discount', models.PositiveIntegerField(default=0, verbose_name='Скидка')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='добавить время')),
                ('quantity_of_products', models.PositiveIntegerField(default=0, verbose_name='Кол-во продуктов')),
                ('products', models.ManyToManyField(to='cart.shoppingcart')),
            ],
            options={
                'verbose_name': 'Позиция заказа',
                'verbose_name_plural': 'Позиция заказа',
            },
        ),
    ]
