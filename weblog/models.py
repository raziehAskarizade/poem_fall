from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.urls import reverse


class TopicManager(models.Manager):
    def get_queryset(self):
        return super(TopicManager, self).get_queryset().filter(status='published')


class Topic(models.Model):
    STATUS_LIST = (('draft', 'ذخیره نشده'), ('published', 'منتشر شده'),)
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    create = models.DateTimeField(auto_now_add=True)
    edit = models.DateTimeField(auto_now=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_LIST, default='draft')
    objects = models.Manager()
    published = TopicManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('weblog:post_detail',
                       args=[self.publish.year,
                             self.publish.month, self.publish.day, self.slug])
