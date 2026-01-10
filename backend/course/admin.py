# course/admin.py
from django.contrib import admin
from .models import Category, Course, Enrollment, Payment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}  # optional if you remove auto-slug in save()

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'current_price', 'language', 'is_published', 'created_at')
    list_filter = ('is_published', 'language', 'category')
    search_fields = ('title', 'description')
    date_hierarchy = 'created_at'

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrolled_at', 'completed', 'progress')
    list_filter = ('completed',)
    search_fields = ('student__user__first_name', 'student__user__last_name', 'course__title')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('student', 'enrollment', 'amount', 'status', 'created_at')
    list_filter = ('status', 'payment_method')
    search_fields = ('student__user__email', 'transaction_id')