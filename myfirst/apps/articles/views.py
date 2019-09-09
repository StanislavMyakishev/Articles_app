from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Article

def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})

def new_article(request):
    return render(request, 'articles/new_article.html')

def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("No such article")

    latest_comments_list = a.comment_set.order_by('-id')[:10]

    return render(request, 'articles/details.html', {'article': a, 'latest_comments_list': latest_comments_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404("No such article")

    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)) )

def add_article(request):
    try: 
        a = Article(article_title = request.POST['article_title'], article_text = request.POST['article_text'], pub_date = timezone.now())
    except:
        raise Http404("No such article")
    a.save()
    return HttpResponseRedirect( reverse('articles:detail', args = (a.id,)))