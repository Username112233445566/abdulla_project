from rest_framework import serializers
from .models import Category, Lesson, WatchHistory

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class WatchHistorySerializer(serializers.ModelSerializer):
    lesson = LessonSerializer()

    class Meta:
        model = WatchHistory
        fields = ('lesson', 'watched_at')