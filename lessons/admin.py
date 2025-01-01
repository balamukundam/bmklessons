from django.contrib import admin

# Register your models here.
from .models import Lesson
from .models import Category
from .models import Book

admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Book)
