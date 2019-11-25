from django.contrib import admin

from .models import Book, Author,BookGanre ,Ganre

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(BookGanre)
admin.site.register(Ganre)
