# course/admin.py
from django.contrib import admin
from .models import Category, Course, Module, Lesson


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1
    fields = ('title', 'order', 'lesson_type', 'duration_minutes', 'is_preview', 'video_url')
    ordering = ('order',)


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1
    fields = ('title', 'order', 'is_free_preview')
    ordering = ('order',)
    show_change_link = True


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'instructor', 'current_price', 'language', 'level',
        'is_published', 'module_count', 'created_at'
    )
    list_filter = ('is_published', 'level', 'language', 'category')
    search_fields = ('title', 'description', 'instructor__first_name', 'instructor__last_name')
    date_hierarchy = 'created_at'
    inlines = [ModuleInline]
    readonly_fields = ('slug', 'created_at', 'updated_at', 'current_price', 'has_discount')
    fieldsets = (
        ('Basic Info', {
            'fields': ('title', 'slug', 'instructor', 'category', 'language', 'level', 'is_published')
        }),
        ('Pricing', {
            'fields': ('price', 'discount_price', 'current_price', 'has_discount')
        }),
        ('Media', {
            'fields': ('thumbnail', 'trailer_url')
        }),
        ('Content', {
            'fields': ('description', 'what_you_will_learn', 'requirements')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def module_count(self, obj):
        return obj.modules.count()
    module_count.short_description = "Modules"


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'is_free_preview', 'lesson_count')
    list_filter = ('course', 'is_free_preview')
    search_fields = ('title', 'course__title')
    inlines = [LessonInline]

    def lesson_count(self, obj):
        return obj.lessons.count()
    lesson_count.short_description = "Lessons"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'icon')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'order', 'lesson_type', 'duration_minutes', 'is_preview')
    list_filter = ('lesson_type', 'module__course', 'is_preview')
    search_fields = ('title', 'module__title', 'module__course__title')
    readonly_fields = ('slug', 'order')