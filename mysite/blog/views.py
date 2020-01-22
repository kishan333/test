from django.shortcuts import render
from django.view.generic import (
	CrerateView,
	DetailView,
	ListView,
	UpdateView,
	DeleteView

)
# Create your views here.
from .models import Article

class ArticlesListView(ListView):
	template_name = 'articles/article_list.html'
	queryset = Article.objects.all()
