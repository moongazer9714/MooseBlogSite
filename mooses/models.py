from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['title']


class Category(models.Model):
    title = models.CharField(max_length=222, blank=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=222, blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='articles')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=222, blank=True)
    email = models.EmailField()
    website = models.CharField(max_length=222, blank=True)
    message = models.CharField(max_length=222, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class About(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=222)
    image = models.ImageField(upload_to='author')
    subtitle = models.TextField()
    title = models.CharField(max_length=222)
    description = models.TextField()
    social_media = models.CharField(max_length=222)

    def __str__(self):
        return self.title


