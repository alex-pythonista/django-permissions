from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Brand(models.Model):
    name = models.CharField(max_length=150)
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Outlet(models.Model):
    name = models.CharField(max_length=150)
    menu = models.ForeignKey("Menu", on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, blank=True, null=True)
    staff = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.brand.name} - {self.name}'


class Items(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(max_length=150)
    note = models.TextField(blank=True, null=True)
    items = models.ManyToManyField(Items)
    def __str__(self):
        return self.name



