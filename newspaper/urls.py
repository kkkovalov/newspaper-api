from django.urls import path
from newspaper import views

urlpatterns = [
    path('', views.homeView, name='home-view'),
    
    # path('test/', views.user_views.testAPI),
    
    path('user/verify/', views.user_views.verifyUserExists, name='user-verify'),
    path('user/login/', views.user_views.loginUser, name='user-login'),
    path('user/register/', views.user_views.registerUser, name='user-register'),
    path('user/update/', views.user_views.updateUser, name='user-update'),
    
    
    path('articles/', views.article_views.articlesView, name="articles-view"),
    path('articles/<str:slug_name>/', views.article_views.singleArticleView, name='single-article-view'),
    
    path('topics/', views.article_views.topicView, name='topic-view'),
    
    path('creators/<str:username>/', views.article_views.creatorView, name='creator-view'),
]
