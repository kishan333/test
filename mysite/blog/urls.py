from django.urls import path
from .views import (
	ArticleDetailView
)

app_name = 'articles'
urlpatterns = [
	path('', ArticleListView.as_view(), name='article-list')
]