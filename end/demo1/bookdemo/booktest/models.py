from django.db import models


# Create your models here.


# 在此处编写应用模型
# 1 注册模型 在setting.py 中的INSTALLED_APPS 添加应用名
# 2 生成迁移文件 用于与数据库交互 python manage.py makemigrations 会在对应的应用下方生成迁移文件
# 3 执行迁移 会在对应的数据库中生成对应的表 python manage.py migrate
# 模型更改之后需要再次生成迁移文件 执行迁移

class Book(models.Model):
    """
    book继承了model类 应为model类拥有操作数据库的功能
    """
    title = models.CharField(max_length=20)
    price = models.FloatField(default=0)
    # default 代表默认值
    pub_date = models.DateField(default="1983-06-01")

    def __str__(self):
        return self.title


class Hero(models.Model):
    name = models.CharField(max_length=20)
    # choices 元组，有几个值写几个
    gender = models.CharField(max_length=6, choices=(('male', '男'), ('female', '女')), default="male")
    content = models.CharField(max_length=100)
    # book 是一对多的外键 on_dekete代表删除主表数据
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# django orm关联查询
# 多方Hero 一方Book
# 1多找一，多方对象 关联字段  exp：h1.book
# 2 一找多, 一方对象。小写对方类名_set.all() exp: b1.hero_set.all()
