from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название аптеки")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True, null=True)
    rent_contract = models.FileField(upload_to='contracts/', blank=True, null=True, verbose_name="Договор аренды (PDF/Word)")
    cadastral_number = models.CharField(max_length=100, verbose_name="Кадастровый номер", blank=True, null=True)
    image = models.ImageField(upload_to='branches/', blank=True, null=True, verbose_name="Фото аптеки")
    opened_date = models.DateField(verbose_name="Дата открытия", blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"


