from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'article', ArticleView, basename='article')
urlpatterns = [
    path('', blog , name = 'blog'),
    path('single_blog/<int:blog_id>/' ,  single_blog , name='single_blog')  ,
    path('search_blog/', search_blog , name = 'search_blog'),
    path('api/', ArticleView.as_view(), name = 'article-list'),
    path('cmapi/', CommentView.as_view(), name = 'comment_list'),
    path('cmapi/<int:pk>/', CommentDetailView.as_view(), name = 'comment_permission')
    
]