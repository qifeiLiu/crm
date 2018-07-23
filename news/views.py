from django.shortcuts import render
from django.http import HttpResponse
from news.models import  Coloumn,Article
# Create your views here.


# def index(request):
#     return HttpResponse(u'欢迎学习django')
def index(request):
    columns = Coloumn.objects.all()
    return render(request, 'index.html', {'columns': columns})
# def column_detail(request,column_slug):
#     return HttpResponse('column_slug:'+column_slug)
#
# def article_detail(request,article_slug):
#     return HttpResponse('article_slug:'+article_slug)

def column_detail(request, column_slug):
    column = Coloumn.objects.get(slug=column_slug)
    num = 1
    return render(request, 'news/column.html',locals())


def article_detail(request, article_slug):
    article = Article.objects.filter(slug=article_slug)[0]
    return render(request, 'news/article.html', {'article': article})
