from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article


class ArticleCreate(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content']

    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArticleDetail(DetailView):
    model = Article

class ArticleList(ListView):
    model = Article

class ArticleUpdate(LoginRequiredMixin,UpdateView):
    model = Article
    fields = ['title', 'content']

class ArticleDelete(LoginRequiredMixin,DeleteView):
    model = Article
    success_url = reverse_lazy('article_list')
