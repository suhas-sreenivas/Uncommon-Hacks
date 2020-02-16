from rest_framework import serializers
from restapi.models import Comics

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comics
        fields = ['title', 'date', 'chapter', 'image']