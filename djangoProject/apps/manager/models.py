from django.db import models
from django.urls import reverse


class Manager(models.Model):
    surname = models.CharField('Фамилия менеджера', max_length=30)
    name = models.CharField('Имя менеджера', max_length=20)
    name_second = models.CharField('Отчество менеджера', max_length=20)
    date_of_birth = models.DateField('Дата рождения')
    address = models.CharField('Адрес проживания', max_length=150)
    data_of_hiring = models.DateField('Дата принятия на работу')

    def __str__(self):
        return self.surname

    def get_absolute_url(self):  # Тут мы создали новый метод
        return reverse('manager_url:manager_detail_view', args=[str(self.id)])

    class Meta:
        verbose_name = 'Менежер'
        verbose_name_plural = 'Менежеры'
