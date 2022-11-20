from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book
#I INSERTED THIS
from .models import Comment

admin.site.register(MainMenu)
admin.site.register(Book)

#Inserted this
admin.site.register(Comment)