from rest_framework import serializers

from reviews.models import User, Category, Genre, Title, Review, Rating


class UserSerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = User

class CategorySerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = Review                 


class RatingSerializer(serializers.ModelSerializer):
  
    class Meta:
        fields = '__all__'
        model = Rating