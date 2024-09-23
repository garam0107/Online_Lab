from django.db import models

# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    title = models.TextField()
    pubdate = models.DateField()
    author = models.TextField()
    pricesales = models.IntegerField()
    adult = models.BooleanField()
    publisher = models.TextField()
    salesPoint = models.IntegerField()
    