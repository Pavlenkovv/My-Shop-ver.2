from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва категорії")
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Категорія", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Найменування')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Зображення")
    description = models.TextField(verbose_name="Опис", null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Ціна")

    def __str__(self):
        return self.title


class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Діагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    processor_freq = models.CharField(max_length=255, verbose_name='Частота процесора')
    ram = models.CharField(max_length=255, verbose_name="Оперативна пам'ять")
    video = models.CharField(max_length=255, verbose_name='Відеокарта')
    time_without_charge = models.CharField(max_length=255, verbose_name='Чаз автономної роботи')

    def __str__(self):
        return f'{self.category.name} : {self.title}'


class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name='Діагональ')
    display_type = models.CharField(max_length=255, verbose_name='Тип дисплея')
    resolution = models.CharField(max_length=255, verbose_name='Розширення екрану')
    accum_volume = models.CharField(max_length=255, verbose_name='Об\'єм батареї')
    ram = models.CharField(max_length=255, verbose_name="Оперативна пам'ять")
    sd = models.BooleanField(default=True, verbose_name="Слот для карт пам\'яті")
    sd_volume_max = models.CharField(max_length=255, verbose_name='Максимальний об\'єм карти пам\'яті')
    main_cam_mp = models.CharField(max_length=255, verbose_name='Головна камера')
    frontal_cam_mp = models.CharField(max_length=255, verbose_name='Фронтальна камера')

    def __str__(self):
        return f'{self.category.name} : {self.title}'


class CardProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Покупець', on_delete=models.CASCADE)
    card = models.ForeignKey('Card', verbose_name='Кошик', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Загальна сума')

    def __str__(self):
        return f'Продукт {self.product.title}'


class Card(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Власник', on_delete=models.CASCADE)
    products = models.ManyToManyField(CardProduct, blank=True, related_name='related_card')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Загальна вартість')

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name='Покупець', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефону')
    address = models.CharField(max_length=255, verbose_name='Адреса')

    def __str__(self):
        return f'Покупець: {self.user.first_name} {self.user.last_name}'

# class Specification(models.Model):
#
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     name = models.CharField(max_length=255, verbose_name="Ім'я товару для характеристик")
#
#     def __str__(self):
#         return f'Характеристики для товару: {self.name}'
