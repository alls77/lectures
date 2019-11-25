from django.db import models


#Inheritance
class User(models.Model):
    last_name = models.harField(max_length=64, blank=True)

    # class Meta: #abstr.inherit
    #     abstract = True #not save in db; only django class
    class Meta: 
        ordering = ['last_name']


class Author(User):
    first_name = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['-first_name']
        db_table = 'test' #'{app_name}_{model_name}' - default
        unique_together = ('first_name', 'last_name')

class UaAuthor(Author):

    class Meta: #proxi inherit
        proxy = True


class Ganre(models.Model):
    name = models.CharField(max_length=64)


class BookManager(models.Manager):
    def author1(self):
        return self.get_queryset().filter(first_name='author')

    def query_set(self):
        return super().get_queryset().order_by('title')


class Book(models.Model):
    title = models.CharField(max_length=64, blank=True) 
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') # book_set == books; name dlya obratnoy svyaz.
    ganres = models.ManyToManyField(Ganre, related_name='books', through='BookGanre')

    man = BookManager()


class BookGanre(models.Model):  # castom many-to-many table
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    ganre = models.ForeignKey(Ganre, on_delete=models.CASCADE)

    date_add = models.DateField(auto_now_add=True)


