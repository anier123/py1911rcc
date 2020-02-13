from django.shortcuts import render
from django.template import loader
from .models import Book, Hero

# Create your views here.

# 编写对应的视图函数
from django.http import HttpResponse


def index(request):
    # return HttpResponse("这里是首页")
    # 1获取模板
    # template = loader.get_template('index.html')
    book = Book.objects.all()
    # 2渲染模板数据
    # context = {'books': book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'index.html', {'books': book})


def detail(request, bookid):
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {'books': book}
    # result = template.render(context)
    # return HttpResponse(result)
    return render(request, 'detail.html', {'books': book})


def about(request):
    return HttpResponse("这里是关于页面")
