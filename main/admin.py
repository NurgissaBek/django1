from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug'] # отображение полей в админке
    prepopulated_fields = {'slug': ('name',)} # автоматическое заполнение поля slug на основе поля name

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available', 'created', 'updated']
    list_filter=['available', 'created', 'updated', 'category'] #фильтрация по этим полям
    list_editable=['price', 'available']
    prepopulated_fields = {'slug': ('name',)}

# Register your models here.
