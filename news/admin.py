from django.contrib import admin
from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at')
    list_display_links = ('id', 'title')
    search_fields = 'title' , 'content'
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id')
admin.site.register(News, NewsAdmin)
admin.site.register(Category)

