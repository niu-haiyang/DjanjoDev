from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=50)
    hero_name = models.CharField(max_length=50)
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hero(models.Model):
    name = models.CharField(max_length=50)
    gender = models.BooleanField()
    book_id = models.ForeignKey('Book', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
