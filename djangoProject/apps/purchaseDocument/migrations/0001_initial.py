# Generated by Django 3.1.4 on 2021-01-12 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата покупки')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('goods_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
            ],
            options={
                'verbose_name': 'Приходная накладная',
                'verbose_name_plural': 'Приходные накладные',
            },
        ),
    ]
