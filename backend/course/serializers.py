# course/serializers.py
from rest_framework import serializers
from .models import Category, Course, Enrollment, Payment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']
        read_only_fields = ['slug']


class CourseListSerializer(serializers.ModelSerializer):
    """Used for list views – lighter payload"""
    instructor_name = serializers.CharField(source='instructor.__str__', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'title', 'slug', 'instructor_name', 'description', 'price',
            'discount_price', 'current_price', 'has_discount', 'language',
            'thumbnail', 'is_published', 'category_name', 'created_at'
        ]


class CourseDetailSerializer(serializers.ModelSerializer):
    """Used for detail/retrieve – can include more data"""
    instructor_name = serializers.CharField(source='instructor.__str__', read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'  # or list all + exclude sensitive ones


class EnrollmentSerializer(serializers.ModelSerializer):
    course_title = serializers.CharField(source='course.title', read_only=True)
    student_name = serializers.CharField(source='student.__str__', read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id', 'student', 'student_name', 'course', 'course_title',
            'enrolled_at', 'completed', 'progress'
        ]
        read_only_fields = ['enrolled_at']


class PaymentSerializer(serializers.ModelSerializer):
    enrollment_info = serializers.CharField(source='enrollment.__str__', read_only=True)

    class Meta:
        model = Payment
        fields = [
            'id', 'enrollment', 'enrollment_info', 'student', 'amount',
            'currency', 'payment_method', 'transaction_id', 'status',
            'created_at', 'paid_at', 'proof_file'
        ]
        read_only_fields = ['created_at', 'paid_at']