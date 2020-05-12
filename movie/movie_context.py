from .models import Movie

def movie_sliders(request):
    movies = Movie.objects.all().order_by('-created')[:3]
    return {
        'movie_sliders':movies
    }