from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home-view'),
    path('login/', views.loginUser, name='login-user'),
    path('articles/', views.articlesView, name="articles-view"),
    path('articles/<str:id>/', views.singleArticleView, name='single-article-view'),
    path('articles/<str:topic>/', views.articlesByTopicView, name='articles-by-topic-view'),
    path('creators/<str:username>/', views.creatorView, name='creator-view'),
]
