from django.db import models
from django.urls import reverse


class Goods(models.Model):
    name = models.CharField('Название товара', max_length=70)
    category = models.CharField('Категория товара', max_length=50)
    count = models.IntegerField('Количество доступного товара', default=0)
    prise = models.IntegerField('Стоимость товара', default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('goods_url:goods_detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
