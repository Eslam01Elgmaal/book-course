# enrollments/api_urls.py
from rest_framework.routers import DefaultRouter
from .views import EnrollmentViewSet, LessonProgressViewSet

router = DefaultRouter()
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'lesson-progress', LessonProgressViewSet, basename='lessonprogress')

urlpatterns = router.urls