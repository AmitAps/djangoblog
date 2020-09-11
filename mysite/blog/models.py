from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    #unique_for_date parameter to this field so that you can build URLs for posts using their publish date and slug . Django will prevent multiple posts from having the same slug for a given date.
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.ForeignKey.on_delete .
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #This field shows the status of a post. You use a choices parameter, so the value of this field can only be set to one of the given choices.
    #https://docs.djangoproject.com/en/3.0/ref/models/fields/
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title
