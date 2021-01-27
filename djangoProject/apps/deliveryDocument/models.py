from django.db import models
from django.urls import reverse


# Накладная на выдачу
class DeliveryDocument(models.Model):
    quantity = models.IntegerField('Количество товара', default=0)
    write_off_document_id = models.ForeignKey('writeOffDocument.WriteOffDocument', on_delete=models.CASCADE, default=0)

    # def __str__(self):
    #     # if self.id == None:
    #     #     return "ERROR-CUSTOMER NAME IS NULL"
    #     return str(self.write_off_document_id.goods_id.name)
    #
    # def __str__(self):
    #     return 'Asentamiento: {} '.format(self.id)

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('delivery_url:delivery_detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = 'Накладная на выдачу'
        verbose_name_plural = 'Накладные на выдачу'
