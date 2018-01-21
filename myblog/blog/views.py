from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    #    return HttpResponse("Hello,World!")
    #    return render(requsest, 'index.html', {'hello': 'Hello,World!!'})
    #    article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


# 第一个参数为对象本身，第二个为模板文件，字符串，第三个参数是后台传递到前端的数据
# Create your views here.

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'article_page.html', {'article': article})


def edit_page(request):
    return render(request, 'edit_page.html')


def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'index.html', {'articles': articles})
