from django.db import models
from django.urls import reverse
# from djangoProject.apps.manager.models import Manager
# from djangoProject.apps.goods.models import Goods


# Накладная на списание
class WriteOffDocument(models.Model):
    date = models.DateField('Дата продажи')
    quantity = models.IntegerField('Количество товара')
    goods_id = models.ForeignKey('goods.Goods', on_delete=models.CASCADE, default=0)
    manager_id = models.ForeignKey('manager.Manager', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.id

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('write_off_url:write_off_detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = 'Накладная на списание'
        verbose_name_plural = 'Накладные на списание'
