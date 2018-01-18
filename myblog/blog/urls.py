from django.urls import path
from . import views

urlpatterns = [
    # URL、响应方法、名称
    #path('index/',bv.index),
    path('', views.index),
]