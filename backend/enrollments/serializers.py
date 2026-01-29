from rest_framework import serializers
from .models import Enrollment, LessonProgress
from course.serializers import CourseListSerializer


class LessonProgressSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)

    class Meta:
        model = LessonProgress
        fields = ['id', 'lesson', 'lesson_title', 'completed', 'completed_at', 'watch_time_seconds']
        read_only_fields = ['completed_at']


class EnrollmentSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    course_title = serializers.CharField(source='course.title', read_only=True)
    student_name = serializers.CharField(source='student.__str__', read_only=True)
    lesson_progress = LessonProgressSerializer(many=True, read_only=True, source='lesson_progress')

    class Meta:
        model = Enrollment
        fields = [
            'id', 'student', 'student_name', 'course', 'course_title',
            'enrolled_at', 'completed', 'progress', 'last_activity', 'lesson_progress'
        ]
        read_only_fields = ['enrolled_at', 'last_activity', 'lesson_progress']