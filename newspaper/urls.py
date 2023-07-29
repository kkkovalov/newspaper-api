from django.urls import path
from newspaper import views

urlpatterns = [
    path('', views.homeView, name='home-view'),
    
    # path('test/', views.user_views.testAPI),
    
    # url to redirect non-creator group users
    path('badrequest/', views.badRequest, name='bad-request'),
    
    # urls for user interaction
    path('user/verify/', views.user_views.verifyUserExists, name='user-verify'),
    path('user/login/', views.user_views.loginUser, name='user-login'),
    path('user/register/', views.user_views.registerUser, name='user-register'),
    path('user/update/', views.user_views.updateUser, name='user-update'),
    
    
    # urls for article interaction for readers
    path('articles/', views.article_views.articlesView, name="articles-view"),
    path('articles/<str:slug_name>/', views.article_views.singleArticleView, name='single-article-view'),
    
    # urls for creator interaction with articles
    path('creator/articles/new', views.creator_views.newArticleView, name='new-article'),
    path('creator/articles/<str:slug_name>', views.creator_views.editArticleView, name='edit-article'),
    
    # urls for topics interaction
    path('topics/', views.topic_views.TopicView.as_view(), name='topic-view'),
]
