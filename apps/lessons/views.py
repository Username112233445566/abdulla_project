from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.utils import timezone
from .models import Category, Lesson, WatchHistory
from django.views.generic import ListView, DetailView, View

class CategoryListView(ListView):
    model = Category
    # Используем путь относительно папки templates в приложении lessons
    template_name = "lessons/lessons_home.html"
    context_object_name = "categories"

class LessonListView(ListView):
    model = Lesson
    # Аналогично, файл lessons_category.html находится в папке lessons/
    template_name = "lessons/lessons_category.html"
    context_object_name = "lessons"

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        self.category = get_object_or_404(Category, id=category_id)
        return Lesson.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class WatchHistoryListView(LoginRequiredMixin, ListView):
    model = WatchHistory
    # Если у вас есть шаблон для истории просмотров, разместите его и укажите путь, например:
    template_name = "lessons/watch_history.html"
    context_object_name = "watch_history"

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user)

class AddToWatchHistoryView(LoginRequiredMixin, View):
    def post(self, request, lesson_id):
        lesson = get_object_or_404(Lesson, id=lesson_id)
        watch_history, created = WatchHistory.objects.get_or_create(
            user=request.user,
            lesson=lesson,
            defaults={'watched_at': timezone.now()}
        )
        if not created:
            watch_history.watched_at = timezone.now()
            watch_history.save()
        return JsonResponse({'status': 'success'})

class ClearWatchHistoryView(LoginRequiredMixin, View):
    def post(self, request):
        WatchHistory.objects.filter(user=request.user).delete()
        return JsonResponse({'status': 'cleared'})

class LessonDetailView(DetailView):
    model = Lesson
    template_name = "lessons/lessons_detail.html"
    context_object_name = "lesson"

