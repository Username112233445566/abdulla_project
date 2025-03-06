from django.urls import path
from .views import CategoryListView, LessonListView, LessonDetailView, WatchHistoryListView, AddToWatchHistoryView, ClearWatchHistoryView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('lessons/<int:category_id>/', LessonListView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('history/', WatchHistoryListView.as_view(), name='watch-history'),
    path('history/add/<int:lesson_id>/', AddToWatchHistoryView.as_view(), name='add-to-history'),
    path('history/clear/', ClearWatchHistoryView.as_view(), name='clear-history'),
]
