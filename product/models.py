from django.db import models


class Category(models.Model):
    parent = models.ForeignKey('Category', verbose_name="Kategoriyasi",
                               null=True, blank=True, on_delete=models.PROTECT)
    name = models.CharField(verbose_name="Kategoriya nomi", max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', verbose_name="Kategoriyasi", on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Maxsulot nomi", max_length=250)
    full_name = models.CharField("Maxsulotning to'liq nomi", max_length=255)
    price = models.DecimalField(verbose_name="Maxsulot narxi", max_digits=17, decimal_places=2)
    describtion = models.TextField(verbose_name="Maxsulot haqida ma'lumot")


    def __str__(self):
        return self.name
