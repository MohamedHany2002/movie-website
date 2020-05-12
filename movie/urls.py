

from django.urls import path
from . import views

urlpatterns = [
    # path('search/',views.Search,name='search'),
    path('search/',views.SearchList.as_view(),name='search'),
    path('',views.MovieList.as_view(),name='MovieList'),
    path('<int:pk>/',views.MovieDetail.as_view(),name='MovieDetail'),
    path('<str:category>/',views.GenereList.as_view(),name='categoryList'),
    path('language/<str:language>/',views.LanguageList.as_view(),name='LanguageList'),
    path('year/<str:year>/',views.YearList.as_view(),name='YearList'),
] 
