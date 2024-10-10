from django.db import models
from django.urls import reverse
from django.conf import settings
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'pk': self.pk})
    
    class Meta:
        verbose_name_plural = "Categories"


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField(blank=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    modification_datetime = models.DateTimeField(auto_now=True)
    publication_datetime = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[
        ('draft', 'Draft'),
        ('published', 'Published')
    ], default='draft')
    slug = models.SlugField(max_length=200, unique=True)
    categories = models.ManyToManyField(Category, related_name='articles')

    def publish(self):
        self.published_date = timezone.now()
        self.status = 'published'
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-modification_datetime']
