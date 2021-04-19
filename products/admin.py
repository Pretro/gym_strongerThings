from django.contrib import admin
from .models import Category, Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'rating', 'sku', 'category', 'image')
    prepopulated_fields = {'friendly_name': ('name')}

    ordering = ('sku')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
