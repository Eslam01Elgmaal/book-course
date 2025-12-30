from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    
    path('register/', RegisterView.as_view(), name='student-register'),
    path('login/', LoginView.as_view(), name='student-login'),
    path('logout/', LogoutView.as_view(), name='student-logout'),

]