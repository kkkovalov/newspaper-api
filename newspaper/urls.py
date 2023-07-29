from django.urls import path
from newspaper import views

urlpatterns = [
    path('', views.homeView, name='home-view'),
    
    # path('test/', views.user_views.testAPI),
    
    path('verify/', views.user_views.verifyUserExists, name='verify-user'),
    path('login/', views.user_views.loginUser, name='login-user'),
    path('register/', views.user_views.registerUser, name='register-user'),
    
    
    path('articles/', views.article_views.articlesView, name="articles-view"),
    path('articles/<str:id>/', views.article_views.singleArticleView, name='single-article-view'),
    
    path('topics/', views.article_views.topicView, name='topic-view'),
    
    path('creators/<str:username>/', views.article_views.creatorView, name='creator-view'),
]
