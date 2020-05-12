from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Movie,Tag
from .models import DownloadLink,genere
from django.db.models import Count

# Create your views here.

class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'movies/index.html'
    def get_context_data(self,**kwargs):
        context = super(MovieList,self).get_context_data(**kwargs)
        generes = genere.objects.values_list('category',flat=True)
        context['generes'] = generes
        context['dates'] = Movie.objects.values_list('year_production',flat=True)
        context['most_watched'] = Movie.objects.all().order_by('-views_count')[:6]
        print(context['dates'])
        return context

class MovieDetail(DetailView): 
    model = Movie
    context_object_name = 'movie'
    template_name = 'movies/single.html'

    def get_object(self):
        obj = super(MovieDetail,self).get_object()
        return obj

    def get_context_data(self,**kwargs):
        context = super(MovieDetail,self).get_context_data(**kwargs)
        context['links']=DownloadLink.objects.filter(movie=self.get_object())
        obj=self.get_object()
        obj.views_count +=1
        obj.save()
        categories = obj.generes.values_list('category',flat=True)
        # context['related_movies']=Movie.objects.filter(generes__category__in=categories).exclude(id=obj.id)
        tags_name = Tag.objects.filter(movie=obj)
        tags_name=tags_name.values_list('name',flat=True)
        # tags_name=obj.tags.values_list('name',flat=True)
        print(tags_name)
        movies = Movie.objects.filter(tags__name__in=tags_name).distinct()
        print(movies,'movies')
        context['related_movies']=movies.annotate(c=Count('tags')).order_by('-c').exclude(id=obj.id) # sort
        return context

class GenereList(ListView):
    model = Movie
    context_object_name = 'movies'

    template_name='movies/genre.html'

    def get_context_data(self,**kwargs):
        category=self.kwargs['category']
        context = super(GenereList,self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(generes__category=category)
        context['category'] = category
        print(context['movies'])
        return context

class LanguageList(ListView):
    print('here')
    model = Movie
    context_object_name = 'movies'
    template_name='movies/index.html'

    def get_context_data(self,**kwargs):
        language=self.kwargs['language']
        context = super(LanguageList,self).get_context_data(**kwargs)
        context['movies'] = Movie.objects.filter(language=language)
        context['language'] = language
        print('ok')
        return context

class SearchList(ListView):
    model = Movie
    template_name = 'movies/index.html'
    context_object_name = 'movies'

    def get_queryset(self):
        query=self.request.GET.get('q')
        print(query)
        print('lol')
        qs = Movie.objects.filter(title__icontains=query)
        return qs

def Search(request):
    print('sdfds')
    query=request.GET.get('q')
    print(query)
    qs = Movie.objects.filter(title__icontains=query)
    print(qs,"ws")
    return render(request,"movies/index.html",{'movies':qs})

 
class YearList(ListView):
    model = Movie
    template_name = "movies/index.html"
    context_object_name = 'movies'

    def get_queryset(self,**kwargs):
        year=self.kwargs['year']
        qs = Movie.objects.filter(year_production__year=year)
        return qs


