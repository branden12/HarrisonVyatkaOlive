from django.contrib import admin

# Register your models here.

from .models import MainMenu
from .models import Book

#Inserted Feature Models
from .models import Comment
from .models import Favorite

admin.site.register(MainMenu)
admin.site.register(Book)

# Registering features Models
admin.site.register(Comment)
admin.site.register(Favorite)