from django.shortcuts import render
from . import models
from django.http import HttpResponseRedirect


def index(request):
    #    return HttpResponse("Hello,World!")
    #    return render(requsest, 'index.html', {'hello': 'Hello,World!!'})
    #    article = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()

    # return HttpResponseRedirect('')
    return render(request, 'blog/index.html', {'articles': articles})


def index_1(request):
    return render(request, 'blog/index_1.html')


# 第一个参数为对象本身，第二个为模板文件，字符串，第三个参数是后台传递到前端的数据
# Create your views here.

def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')

    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit_page.html', {'article': article})


def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    article_id = request.POST.get('article_id', '0')

    if article_id == '0':
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article_page.html', {'article': article})
