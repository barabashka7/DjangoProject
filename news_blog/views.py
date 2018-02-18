from django.http import HttpResponseNotFound,HttpResponse
from .models import Article, Author, Comment
from .forms import ArticleForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

# Create your views here.

def index(request):
    articles = Article.objects.all()
    return render(request, 'news_blog/new_list.html', {'articles': articles})

def get_article(request, article_id):
   try:
       article = Article.objects.get(id=article_id)
       author = Author.objects.filter(article__pk=article_id)
       comment = Comment.objects.filter(article__pk=article_id)
   except (Article.DoesNotExist, Author.DoesNotExist) as error:
       return HttpResponseNotFound(error)
   if request.method == "POST":
       form = CommentForm(request.POST)
       if form.is_valid():
            comment = form.save(commit=False)
            comment.published_date = timezone.now()
            comment.article = article
            comment.save()
            return redirect('article', article_id=article.pk)
   else:
        form = CommentForm()
   return render(request, 'news_blog/news_article.html',
                 {'article': article,
                  'author': author,
                  'comment': comment,
                  'form': form
                  }
                 )
def new_article(request):
   if request.method == "POST":
       form = ArticleForm(request.POST)
       if form.is_valid():
           article = form.save(commit=False)
           article.published_date = timezone.now()
           article.save()
           return redirect('article', article_id=article.pk)
   else:
       form = ArticleForm()
   return render(request, 'news_blog/edit_article.html', {'form': form})

def edit_article(request, article_id):
   article = get_object_or_404(Article, pk=article_id)
   if request.method == "POST":
       form = ArticleForm(request.POST, instance=article)
       if form.is_valid():
           article = form.save(commit=False)
           article.published_date = timezone.now()
           article.save()
           return redirect('article', article_id=article.pk)
   else:
       form = ArticleForm(instance=article)
   return render(request, 'news_blog/edit_article.html', {'form': form})
