from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('index/', views.index, name='index'),

]
