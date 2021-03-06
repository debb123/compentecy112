from django.db import models
from django.contrib import admin

# Create your models here.
'''
field:
    char
    int
    Float
    Boolean
'''

# Migration steps
# 1 -Make migrations
# 2 - (migrate) apply migrations

# Create your models here .
class Genre(models.Model):
    name = models.CharField(max_length = 255)

    def _str_(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    star = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    price = models.FloatField()
    in_stock = models.IntegerField()
    # have i to many relations with genre
    genre = models.ForeignKey(Genre, on_delete = models.CASCADE)
    in_4k = models.BooleanField()
    director = models.CharField(max_length = 255)
    image_url = models.TextField()

    #def_str_(self):
    #   return str(self.release_year) + self.title


    # lets say you want tot add a new column for the genre list , to display the ID
    # customise the string representation of the genre objects
    # on models


    ## Customise genre
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


    # create classes to customize how admin display models

class MovieAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'title')
    list_display = ('id','release_year','title','genre')

    #exclude = ('in_stock', 'price')
        #fields = ('genre', 'title', 'director', 'in_stock', 'price')
