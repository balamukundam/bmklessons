from django.db import models
import json

#Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.book_name

class Lesson(models.Model):
    lesson_number = models.PositiveIntegerField()
    book = models.ForeignKey(Book, on_delete=models.DO_NOTHING, null=True)
    
    title = models.CharField(max_length=50)
    json_data = models.TextField()

    def get_json_data(self):
        return json.loads(self.json_data)
    
    def set_json_data(self, data):
        self.json_data = json.dumps(data, indent=4, sort_keys=True)

    data = property(get_json_data, set_json_data)

    def __str__(self):
        return f"{self.lesson_number} | {self.title}"

   