from django.contrib import admin
from lms.models import Course, Lesson


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "preview"]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "video_url", "preview", "course"]
