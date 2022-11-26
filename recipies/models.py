from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    ingredients = models.ManyToManyField(Ingredient)

    def __str__(self):
        return self.name
    


