from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

class Author(models.Model):
    first_name = models.CharField(max_length=64)

    comments = GenericRelation('Comment', related_query_name='author') #object_id_field='' - pk for content type


class Ganre(models.Model):
    name = models.CharField(max_length=64)


# class BookManager(models.Manager):
#     def author1(self):
#         return self.get_queryset().filter(first_name='author')

#     def query_set(self):
#         return super().get_queryset().order_by('title')


class Book(models.Model):
    title = models.CharField(max_length=64, blank=True) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # book_set == books; 
    ganres = models.ManyToManyField(Ganre, related_name='books', through='BookGanre')

    comments = GenericRelation('Comment') #model name


class BookGanre(models.Model):  # castom many-to-many table
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ganre = models.ForeignKey(Ganre, on_delete=models.CASCADE)

    date_add = models.DateField(auto_now_add=True)

class Comment(models.Model):
    text = models.CharField(max_length=200) 

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()

    content_object = GenericForeignKey('content_type', 'object_id') #no filter
