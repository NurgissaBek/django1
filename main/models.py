from django.db import models

# Create your models here.
# конструкция для образования базы данных, чтобы мы не писали SQL-запросы вручную

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)#  индексируемое поле для ускорения поиска, в основном благодаря db_index=True
    slug = models.SlugField(max_length=100, unique = True)# уникальное поле для формирования ЧПУ url ссылок

    class Meta: #вложенный класс для задания метаданных модели, метаданные нужны для управления поведением модели, например, для задания порядка сортировки записей
        ordering = ('name',)
        verbose_name = 'category' #человеко-читабельное имя
        verbose_name_plural = 'categories' #множественное число

    def __str__(self): #метод для представления объекта модели в виде строки
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) #связь многие ко многим, при удалении категории удаляются и товары
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True) # slug - для формирования ЧПУ url ссылок к примеру /product/some-product-name
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #поле для загрузки изображений товаров
    description = models.TextField(blank=True) #blank=True - поле не обязательное для заполнения
    price = models.DecimalField(max_digits=10, decimal_places=2) # max_digits - всего цифр, decimal_places - цифры после запятой
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


