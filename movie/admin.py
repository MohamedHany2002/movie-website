from django.contrib import admin
from .models import Movie,DownloadLink,Participant,genere,Tag
# Register your models here.
admin.site.register(Movie)
admin.site.register(DownloadLink)
admin.site.register(Participant)
admin.site.register(genere)
admin.site.register(Tag)