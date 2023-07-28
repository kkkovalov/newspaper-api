from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homeView, name='home-view'),
    
    path('verify/', views.verifyUserExists, name='verify-user'),
    path('login/', views.loginUser, name='login-user'),
    path('register/', views.registerUser, name='register-user'),
    
    
    path('articles/', views.articlesView, name="articles-view"),
    path('articles/<str:id>/', views.singleArticleView, name='single-article-view'),
    
    path('topics/', views.topicView, name='topic-view'),
    
    path('creators/<str:username>/', views.creatorView, name='creator-view'),
]
