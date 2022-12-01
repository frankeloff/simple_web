from django.db import models
from django.urls import reverse

# Create your models here.

class Firm(models.Model):
    firm_name = models.TextField(blank=False, verbose_name="Название фирмы")
    def __str__(self):
        return self.firm_name

class Rate(models.Model):
    rate_name = models.TextField(blank=False, verbose_name="Название тарифа")
    
    def __str__(self):
        return self.rate_name

class Car(models.Model):
    car_name = models.TextField(blank=False, verbose_name="Название тарифа")
    
    def __str__(self):
        return self.car_name

    def get_absolute_url(self):
        return reverse('views_car', kwargs={"pk": self.pk})

class Price(models.Model):
    firm = models.ForeignKey(
        "Firm", on_delete=models.PROTECT, verbose_name="Фирма"
    )
    rate = models.ForeignKey(
        "Rate", on_delete=models.PROTECT, verbose_name="Фирма"
    )
    car = models.ForeignKey(
        "Car", on_delete=models.PROTECT, verbose_name="Фирма"
    )
    price = models.IntegerField(blank=False, verbose_name="Цена")
