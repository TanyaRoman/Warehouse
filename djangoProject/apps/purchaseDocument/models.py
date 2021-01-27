from django.db import models
from django.urls import reverse
# from djangoProject.apps.manager.models import Manager
# from djangoProject.apps.goods.models import Goods


# Приходная накладная
class PurchaseDocument(models.Model):
    date = models.DateField('Дата покупки')
    quantity = models.IntegerField('Количество товара')
    goods_id = models.ForeignKey('goods.Goods', on_delete=models.CASCADE, default=0)
    manager_id = models.ForeignKey('manager.Manager', on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.id

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('purchase_url:purchase_detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = 'Приходная накладная'
        verbose_name_plural = 'Приходные накладные'
