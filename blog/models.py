from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    email_address = models.EmailField(unique=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title = models.CharField(max_length=50, validators=[MinLengthValidator(2)])
    excerpt = models.TextField()
    image_name = models.CharField(max_length=50)
    date = models.DateField()
    slug = models.SlugField(unique=True, blank=True, null=False, db_index=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return f"{self.title} ({self.author})"