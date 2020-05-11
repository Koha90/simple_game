from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # Поле заголовка статьи
    title = models.CharField(max_length=250)
    # Поле для формирования URL понятных человеку.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # Автор. Тут и так всё понятно.
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # Основное содержание статьи
    body = models.TextField()
    # Поле даты, которое сохраняет дату публикации статьи
    publish = models.DateTimeField(default=timezone.now)
    # Поле, которое указывает, когда статья была создана
    created = models.DateTimeField(auto_now_add=True)
    # Когда статья была обновлена
    updated = models.DateTimeField(auto_now=True)
    # Статус статьи
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
