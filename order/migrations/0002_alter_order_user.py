# Generated by Django 4.0.4 on 2022-06-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(max_length=155, verbose_name='Пользователь'),
        ),
    ]