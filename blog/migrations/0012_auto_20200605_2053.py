# Generated by Django 2.2.12 on 2020-06-05 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200605_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='parceiro',
            name='bairro',
            field=models.CharField(default=2, max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='email',
            field=models.EmailField(max_length=300),
        ),
        migrations.AlterField(
            model_name='parceiro',
            name='rua',
            field=models.CharField(max_length=300),
        ),
    ]