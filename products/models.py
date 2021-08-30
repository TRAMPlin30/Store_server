from django.db import models

# Create your models here.
from users.models import User


class ProductCategory(models.Model):
    name = models.CharField(max_length=64, unique=True)
    discription = models.TextField(blank=True) # типа может быть пустым

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='products_images', blank=True) # не работает без библиотеки Pillow
    discription = models.TextField(blank=True)
    short_discription = models.CharField(max_length=64, blank=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2) # до запятой и после запятой
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE) # если PROTECT невозможно удалить категорию пока к ней привязан хотябы один из продуктов

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} | {self.category.name}'



class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    # данная переменная нужна для отслеживания времени, когда появляется объект класса в котором она находиться

    def __str__(self):
        return f'Корзина для: {self.user.name} | Продукт: {self.product.name}'

    def sum(self):
        return self.quantity * self.product.price
