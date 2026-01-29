from rest_framework import serializers
from .models import Category, Course, Module, Lesson


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'icon']
        read_only_fields = ['slug']


class LessonListSerializer(serializers.ModelSerializer):
    """Light version for lists (e.g. inside module preview)"""
    class Meta:
        model = Lesson
        fields = [
            'id', 'title', 'slug', 'order', 'lesson_type',
            'duration_minutes', 'is_preview'
        ]


class LessonDetailSerializer(serializers.ModelSerializer):
    """Full version for lesson detail view"""
    video_file_url = serializers.FileField(source='video_file', read_only=True)

    class Meta:
        model = Lesson
        fields = [
            'id', 'title', 'slug', 'order', 'lesson_type', 'duration_minutes',
            'video_url', 'video_file_url', 'external_url', 'file',
            'content', 'is_preview'
        ]
        read_only_fields = ['slug', 'order', 'video_file_url']


class ModuleListSerializer(serializers.ModelSerializer):
    """Light version for module list (e.g. inside course)"""
    lesson_count = serializers.IntegerField(source='lessons.count', read_only=True)

    class Meta:
        model = Module
        fields = ['id', 'title', 'slug', 'order', 'is_free_preview', 'lesson_count']


class ModuleDetailSerializer(serializers.ModelSerializer):
    """Full version with nested lessons"""
    lessons = LessonDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Module
        fields = [
            'id', 'title', 'slug', 'order', 'description',
            'is_free_preview', 'lessons'
        ]
        read_only_fields = ['slug', 'order', 'lessons']


class CourseListSerializer(serializers.ModelSerializer):
    """Light version for course list view (search, browse)"""
    instructor_name = serializers.CharField(source='instructor.__str__', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True, allow_null=True)
    module_count = serializers.IntegerField(source='modules.count', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'instructor_name', 'category_name',
            'description', 'price', 'discount_price', 'current_price',
            'has_discount', 'language', 'level', 'thumbnail', 'trailer_url',
            'is_published', 'created_at', 'module_count'
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """Full version for course detail (includes modules + preview lessons)"""
    instructor_name = serializers.CharField(source='instructor.__str__', read_only=True)
    category = CategorySerializer(read_only=True, allow_null=True)
    modules = ModuleListSerializer(many=True, read_only=True)  # light modules

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'instructor_name', 'category', 'description',
            'what_you_will_learn', 'requirements', 'price', 'discount_price',
            'current_price', 'has_discount', 'language', 'level',
            'thumbnail', 'trailer_url', 'is_published', 'created_at', 'updated_at',
            'modules'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'modules']