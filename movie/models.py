from django.db import models
from datetime import datetime

# Create your models here.


CATEGORY_CHOICES=(('A','action'),('D','drama'),('C','comedy'),('R','romance'),)
languages_choices=(('A','arabic'),('E','english'),('G','german'),('C','chinese'),)
status_choices=(('RA','recently added'),('mv','most viewed'),('TR','top rated'),)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    category = models.CharField(max_length=150,choices=CATEGORY_CHOICES)
    trailer = models.URLField()
    # slug = models.SlugField()
    year_production = models.DateField()
    image = models.ImageField(upload_to='movies/')
    banner_image = models.ImageField(upload_to='sliders/',null=True,blank=True)
    language = models.CharField(max_length=150,choices=languages_choices)
    status = models.CharField(max_length=150,choices=status_choices)
    views_count = models.IntegerField(default=0)
    participants = models.ManyToManyField('Participant',related_name = 'movies',blank=True)
    created = models.DateTimeField(default=datetime.now())

    @property
    def get_year(self):
        return self.year_production.year

    def __str__(self):
        return self.title

roles_choices = (('D','Director'),('A','actors'),('P','producer'),)
class Participant(models.Model):
    Name = models.CharField(max_length=100)
    works = models.TextField()
    role = models.CharField(max_length=100,choices=roles_choices)
    birthDate = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Name + self.role


link_choices = (('W','watch'),('D','download'),)

class DownloadLink(models.Model):
    url = models.URLField()
    movie = models.ForeignKey('movie',on_delete=models.CASCADE,related_name='links')
    type = models.CharField(max_length=100,choices=link_choices)


class genere(models.Model):
    category = models.CharField(max_length=150,choices=CATEGORY_CHOICES)
    movie = models.ForeignKey('movie',on_delete=models.CASCADE,related_name='generes')

class Tag(models.Model):
    name = models.CharField(max_length=100)
    movie = models.ForeignKey('Movie',on_delete=models.CASCADE,related_name='tags',null=True,blank=True)
    

# add most watched ok ok 
# add most related ok ok   .... hint .. most related is not similar movies
# add recommendation get most simialr movies annotate with count of tag
# revise first 2 projects in django by example
# handle base.html