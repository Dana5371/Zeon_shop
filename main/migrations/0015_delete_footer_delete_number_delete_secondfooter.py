# Generated by Django 4.0.4 on 2022-06-12 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_aboutus_options_alter_backcall_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Footer',
        ),
        migrations.DeleteModel(
            name='Number',
        ),
        migrations.DeleteModel(
            name='SecondFooter',
        ),
    ]