from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from restapi.models import Comics
from restapi.serializers import ComicSerializer

@api_view(['GET'])
def comics_list(request):
    if request.method == 'GET':
        comics = Comics.objects.all()
        serializer = ComicSerializer(comics, many = True)
        return Response(serializer.data)