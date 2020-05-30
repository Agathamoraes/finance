# Generated by Django 2.2.12 on 2020-05-29 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('importado', models.BooleanField(default=False)),
                ('ncm', models.CharField(max_length=8, verbose_name='NCM')),
                ('produto', models.CharField(max_length=100, unique=True)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Estoque Atual')),
                ('estoque_minimo', models.PositiveIntegerField(default=0, verbose_name='Estoque Minímo')),
            ],
        ),
    ]
