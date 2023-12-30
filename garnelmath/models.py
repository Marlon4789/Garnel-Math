from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

# clase post
class Post(models.Model):
    title = models.CharField('title', max_length=100)
    description = models.CharField('description', max_length=300)
    content = RichTextField()
    image = models.URLField('image')
    date_created = models.DateField('date_created', auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title