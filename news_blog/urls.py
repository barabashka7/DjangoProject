from django.urls import path
from . import views

urlpatterns = [
path('new/', views.new_article, name='new_article'),
    path('', views.index, name='index'),
    path('<int:article_id>/',views.get_article,name='article'),
    path('<int:article_id>/edit', views.edit_article, name='edit'),
]
