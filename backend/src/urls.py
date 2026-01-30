# src/urls.py
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    # API endpoints from all apps
    path('api/', include('course.api_urls')),
    path('api/', include('enrollments.api_urls')),
    path('api/', include('payments.api_urls')),
    # path('api/', include('instructor.api_urls')),  # if you add
    # path('api/', include('student.api_urls')),

    # Central Swagger
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]