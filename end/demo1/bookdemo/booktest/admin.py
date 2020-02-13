from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import Book, Hero


# 定义关联，使定义书籍的时候可以插入英雄
class HeroInlines(admin.StackedInline):
    model = Hero
    # 指定插入书籍的时候可以同时插入几个英雄
    extra = 1


class BookAdmin(ModelAdmin):
    list_display = ('title', 'price', 'pub_date')

    # 定义后端搜索字段
    search_fields = ('title', 'price')

    # 指定过滤字段
    list_filter = ('title', 'price')
    # 接收定义关联的类
    inlines = [HeroInlines]


admin.site.register(Book, BookAdmin)


class HeroAdmin(ModelAdmin):
    list_display = ('name', 'gender', 'content', 'book')


admin.site.register(Hero, HeroAdmin)
