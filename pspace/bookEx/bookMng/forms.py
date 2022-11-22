from django import forms
from django.forms import ModelForm

from .models import Book, Rate
from .models import Comment


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
        fields = [
            'title',
            'comment',
        ]


class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = [
            'rate'
        ]
