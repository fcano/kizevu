from django.urls import path
from . import views as core_views

urlpatterns = [
    path('', core_views.ArticleList.as_view(), name='article_list'),
	path('articles/', core_views.ArticleList.as_view(), name='article_list'),
	path('article/<int:pk>/', core_views.ArticleDetail.as_view(), name='article_detail'),
	path('article/add/', core_views.ArticleCreate.as_view(), name='article_add'),
	path('article/<int:pk>/edit/', core_views.ArticleUpdate.as_view(), name='article_update'),
	path('article/<int:pk>/delete/', core_views.ArticleDelete.as_view(), name='article_delete'),
]
