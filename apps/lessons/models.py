from django.db import models
from django.contrib.auth import get_user_model
import re

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Lesson(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255)
    video_url = models.URLField()
    
    def __str__(self):
        return self.title

    @property
    def youtube_id(self):
        """
        Извлекает идентификатор видео из стандартной ссылки YouTube.
        Например: https://www.youtube.com/watch?v=ABC123DEF
        """
        regex = r"(?:v=|youtu\.be/)([^&]+)"
        match = re.search(regex, self.video_url)
        if match:
            return match.group(1)
        return ""

class WatchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watch_history')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-watched_at']
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} watched {self.lesson.title}"