from urllib import request
from drf_app.models import Movie
from drf_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(('GET', 'POST'))
def movie_list(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
       serializer = MovieSerializer(data=request.data)
       if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
       else:
          return Response(serializer.errors)
    

@api_view(('GET', 'PUT', 'DELETE'))
def movie_detail(request, pk):
     movie = Movie.objects.get(pk=pk)
     if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data)
     elif request.method == 'PUT':
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
     elif request.method == 'DELETE':
        #  Queryset methodu olduğu için serializers.py içerisine eklemeye gerek yok
         movie.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)