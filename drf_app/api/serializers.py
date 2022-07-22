from dataclasses import fields
from wsgiref.validate import validator
from rest_framework import serializers
from drf_app.models import Movie


# def name_length_check(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short')


# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length_check])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     # .save() methodu ile çağırılır
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     # .save() methodu ile çağırılır
#     # instance = old value
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name')
#         instance.description = validated_data.get('description')
#         instance.active = validated_data.get('active')
#         instance.save()
#         return instance

#     # Object validation
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError(
#                 'Name cannot be equal to description')

#         return data

# Field validation
# def validate_name(self, value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short')

#     return value


class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    
    class Meta():
        model = Movie
        # model.len_name = 'Test'
        fields = '__all__'
        # fields=['id', 'name', 'description']
        # exclude=['active']

    # Object validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                'Name cannot be equal to description')

        return data

    # Field validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short')

        return value
    
    # get + "_" + class attr. ile kullanılırsa otomatik çağırılır
    # object. ile tüm değerlere erişilir
    def get_len_name(self, object):
        return len(object.name)
