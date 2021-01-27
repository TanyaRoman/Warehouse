# Generated by Django 3.1.4 on 2021-01-14 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteOffDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата продажи')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('goods_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='goods.goods')),
                ('manager_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='manager.manager')),
            ],
            options={
                'verbose_name': 'Накладная на списание',
                'verbose_name_plural': 'Накладные на списание',
            },
        ),
    ]