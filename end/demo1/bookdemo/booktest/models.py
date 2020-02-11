from django.db import models


# Create your models here.


# 在此处编写应用模型

class Book(models.Model):
    """
    book继承了model类 应为model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    # default 代表默认值
    pub_date = models.DateField(default="1983-06-01")


class Hero(models.Model):
    name = models.CharField(max_length=20)
    # choices 元组，有几个值写几个
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default="male")
    content = models.CharField(max_length=100)
    # book 是一对多的外键 on_dekete代表删除主表数据
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
