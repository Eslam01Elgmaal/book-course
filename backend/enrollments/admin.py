# enrollments/admin.py
from django.contrib import admin
from .models import Enrollment, LessonProgress


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        'student', 'course', 'enrolled_at', 'completed', 'progress', 'last_activity'
    )
    list_filter = ('completed', 'course__category', 'enrolled_at')
    search_fields = (
        'student__user__first_name', 'student__user__last_name',
        'student__user__email', 'course__title'
    )
    date_hierarchy = 'enrolled_at'
    readonly_fields = ('enrolled_at', 'last_activity')
    list_per_page = 20


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('enrollment', 'lesson', 'completed', 'completed_at', 'watch_time_seconds')
    list_filter = ('completed', 'lesson__module__course')
    search_fields = (
        'enrollment__student__user__first_name',
        'enrollment__student__user__last_name',
        'lesson__title', 'lesson__module__title'
    )
    date_hierarchy = 'completed_at'
    readonly_fields = ('completed_at',)
    list_per_page = 20