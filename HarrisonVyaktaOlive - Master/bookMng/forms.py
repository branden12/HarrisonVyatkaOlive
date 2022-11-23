from django import forms
from django.forms import ModelForm

from .models import Book
from .models import Comment
from .models import Favorite


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields=[
            'title',
            'comment',
           # 'book',
        ]

class FavoriteForm(ModelForm):

    class Meta:
        model = Favorite
        fields =[
            'title'
        ]