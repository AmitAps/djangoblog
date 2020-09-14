from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        """
        The super() function in Python makes class inheritance more manageable and extensible.
        The function returns a temporary object that allows reference to a parent class by the keyword super.
        """
        return super().get_queryset().filter(status='published')


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
    objects = models.Manager() #The default manager.
    published = PublishedManager() #Our custom manager.
    tags = TaggableManager()

    def get_absolute_url(self):
        """
        You will use the get_absolute_url() method in your templates to link to
        specific posts.
        """
        return reverse('blog:post_detail',
                        args=[self.publish.year,
                            self.publish.month,
                            self.publish.day, self.slug])


    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title



class Comment(models.Model):
    """
    Models for comments
    what is related_name?
    """
    #associate a comment with a single post
    post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)
        #No more duplicate comments
        unique_together = [['email', 'body']]

    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
