from rest_framework import serializers
from drf_app.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    # .save() methodu ile çağırılır
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # instance = old value
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.active = validated_data.get('active')
        instance.save()
        return instance