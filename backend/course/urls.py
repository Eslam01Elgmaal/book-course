from rest_framework.routers import DefaultRouter

from .views import (
    CategoryViewSet, CourseViewSet, EnrollmentViewSet, PaymentViewSet
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'payments', PaymentViewSet, basename='payment')

urlpatterns = router.urls