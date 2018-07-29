from django.shortcuts import render,redirect
from django.http import HttpResponse
from news.models import  Coloumn,Article
# Create your views here.


# def index(request):
#     return HttpResponse(u'欢迎学习django')
# def login2(request):
#     return redirect('/login')

def login(request):
    message =''
    if  request.method == 'POST':
        print('%s' %request.POST)
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'root' and pwd == 'root':
             rep = redirect('/index/')
             rep.set_cookie('username',user)
             return rep
        else:
            message ="用户名或密码错误"

    return render(request,'login.html',locals())

def index(request):
    # columns = Coloumn.objects.all()
    username = request.COOKIES.get('username')
    if username:
        home_display_columns = Coloumn.objects.filter(home_display=True)
        nav_display_columns = Coloumn.objects.filter(nav_display=True)
        return render(request, 'index.html', locals())
    else:
        return redirect('/login/')

# def column_detail(request,column_slug):
#     return HttpResponse('column_slug:'+column_slug)
#
# def article_detail(request,article_slug):
#     return HttpResponse('article_slug:'+article_slug)

def column_detail(request, column_slug):
    username = request.COOKIES.get('username')
    if username:
       column = Coloumn.objects.get(slug=column_slug)
       num = 1
       return render(request, 'news/column.html',locals())
    else:
        return redirect('/login/')


def article_detail(request, pk, article_slug):
    username = request.COOKIES.get('username')
    if username:
        article = Article.objects.get(pk=pk)
        if article_slug != article.slug:
            return redirect(article, permanent=True)
        return render(request, 'news/article.html', {'article': article})
    else:
        return redirect('/login/')
