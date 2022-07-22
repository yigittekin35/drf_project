from django.urls import path
# from drf_app.api.views import movie_list, movie_detail
from drf_app.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    path('list', MovieListAV.as_view(), name='movie_list'),
    path('<int:pk>', MovieDetailAV.as_view(), name='movie_detail'),
]
