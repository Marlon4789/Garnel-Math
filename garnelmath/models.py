from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# Modelo post
class Post(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.CharField('description',blank=True, max_length=300)
    content = RichTextField()
    image = models.URLField(blank=True)
    date_created = models.DateField('date_created', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title
    
# Modelo feedback
class Feedback(models.Model):
    feedback = models.TextField('feedback', unique=True)
    date = models.DateField('date', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.feedback
    
# Modelo suscripción
class Subscription(models.Model):
    email = models.EmailField('email', unique=True, max_length=100)
    date = models.DateField('date', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.email