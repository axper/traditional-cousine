from django.db import models


class Location(models.Model):
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200)

    def __str__(self):
        return self.region


class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200, default='Recipe Name')
    description = models.TextField(default='Description Placeholder')
    picture = models.ImageField(null=True, blank=True)
    location = models.ManyToManyField(to=Location)
    ingredients = models.ManyToManyField(to=Ingredient)
    minutes = models.PositiveIntegerField(default=1)
    youtube = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Step(models.Model):
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(max_length=20000, default='Step Description Placeholder')
    picture = models.ImageField(null=True, blank=True)
    recipe = models.ForeignKey(to=Recipe, related_name='steps')
    time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.description[0:20]

    class Meta:
        unique_together = ('order', 'recipe',)
