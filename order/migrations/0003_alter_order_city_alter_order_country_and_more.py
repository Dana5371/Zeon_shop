# Generated by Django 4.0.4 on 2022-06-16 05:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('order', '0002_remove_order_date_of_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=155, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(max_length=200, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=155, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=155, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.shoppingcart'),
        ),
    ]
