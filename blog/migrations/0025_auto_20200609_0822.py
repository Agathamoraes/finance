# Generated by Django 2.2.12 on 2020-06-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200608_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='estoque',
            field=models.IntegerField(verbose_name='estoque atual'),
        ),
    ]
