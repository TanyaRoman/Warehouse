# Generated by Django 3.1.4 on 2021-01-14 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('writeOffDocument', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('write_off_document_id', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='writeOffDocument.writeoffdocument')),
            ],
            options={
                'verbose_name': 'Накладная на выдачу',
                'verbose_name_plural': 'Накладные на выдачу',
            },
        ),
    ]