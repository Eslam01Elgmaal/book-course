from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Enrollment, LessonProgress
from .serializers import EnrollmentSerializer, LessonProgressSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only show user's own enrollments (or admin sees all)
        if self.request.user.is_staff:
            return Enrollment.objects.all()
        return Enrollment.objects.filter(student__user=self.request.user)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['course', 'completed']


class LessonProgressViewSet(viewsets.ModelViewSet):
    serializer_class = LessonProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_staff:
            return LessonProgress.objects.all()
        return LessonProgress.objects.filter(enrollment__student__user=self.request.user)

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['enrollment', 'lesson']