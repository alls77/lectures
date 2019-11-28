from django import forms

from .models import Book


class AuthorForm(forms.Form):
    author_id = forms.IntegerField(min_value=3)

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
