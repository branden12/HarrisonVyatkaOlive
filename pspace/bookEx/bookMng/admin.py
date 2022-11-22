from django.contrib import admin

# Register your models here.

from .models import MainMenu, Rate
from .models import Book
#I INSERTED THIS
from .models import Comment

admin.site.register(MainMenu)
admin.site.register(Book)
admin.site.register(Comment)

#Angy inserted this
admin.site.register(Rate)