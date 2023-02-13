from django.db import models
from django.utils.text import slugify

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=250, verbose_name='Наименование')
    title = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.CharField(max_length=250, verbose_name='Категория')
    price = models.FloatField(verbose_name='Цена за покупку')
    date_create = models.DateTimeField(verbose_name='Дата создания')
    date_update = models.DateTimeField(verbose_name='Дата последнего изменения')


class Meta:
    verbose_name = 'Продукт'
    verbose_name_plural = 'Продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=250, verbose_name='Наименование')
    title = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Blog(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        ('active', "Опубликован"),
        ('inactive', "Не опубликован"),
    )

    head = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.CharField(max_length=250, verbose_name='Slug')
    content = models.TextField(verbose_name='Содержимое')
    image = models.ImageField(upload_to='media/', verbose_name='Изображение', **NULLABLE)
    date_create = models.DateTimeField(verbose_name='Дата создания')
    views_number = models.IntegerField(default=0, verbose_name='Количество просмотров')
    publication = models.CharField(choices=STATUSES, default=STATUS_ACTIVE, max_length=250, verbose_name='Признак публикации')
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.head)
        super(Blog, self).save(*args, **kwargs)

        
class Version(models.Model):
    STATUS_ACTIVE = 'active'
    STATUS_INACTIVE = 'inactive'
    STATUSES = (
        ('active', 'активна'),
        ('inactive', 'неактивна')
    )
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)
    number = models.FloatField(default=1, verbose_name='Номер версии')
    name = models.CharField(max_length=250, verbose_name='Название версии')
    status = models.CharField(choices=STATUSES, default=STATUS_INACTIVE, max_length=50, verbose_name='Признак версии')
    
