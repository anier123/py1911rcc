# 引入路由绑定函数
from django.conf.urls import url
from . import views

# 2.每一个路由文件中必须编写路由数组
urlpatterns = [
    url(r'^index/$', views.index),
    url(r'detail/(\d+)/', views.detail),
    url(r'^about/$', views.about)
]
