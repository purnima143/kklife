from django.db import models

# Create your models here.

class Blog(models.Model):
    author = models.TextField()
    title = models.TextField()
    published_date = models.DateTimeField(auto_now=True)
    blog_content = models.TextField()

class User(models.Model):
    name = models.TextField(null=False, blank=False)
    email = models.TextField(null=False, blank=False)
    ph_no = models.IntegerField(null=False, blank=False)

    any_message = models.TextField()

    

