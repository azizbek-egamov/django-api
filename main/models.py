from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=40)
    rasm = models.ImageField(upload_to="photo")
    slug = models.SlugField(unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    
    def __str__(self) -> str:
        return self.name
    
class Kitob(models.Model):
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    rasm = models.ImageField(upload_to="photo")
    file = models.FileField(upload_to="file")
    created = models.DateTimeField(auto_now_add=True)
    view = models.IntegerField()
    info = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.name
    
class BookDownloads(models.Model):
    count = models.IntegerField()