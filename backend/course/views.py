from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Course, Module, Lesson
from .serializers import (
    CategorySerializer,
    CourseListSerializer, CourseDetailSerializer,
    ModuleListSerializer, ModuleDetailSerializer,
    LessonListSerializer, LessonDetailSerializer
)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CourseListSerializer
        return CourseDetailSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'language', 'level', 'is_published']
    search_fields = ['title', 'description', 'instructor__first_name', 'instructor__last_name']
    ordering_fields = ['created_at', 'price', 'title']


class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return ModuleListSerializer
        return ModuleDetailSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course']


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return LessonListSerializer
        return LessonDetailSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['module', 'module__course', 'lesson_type', 'is_preview']