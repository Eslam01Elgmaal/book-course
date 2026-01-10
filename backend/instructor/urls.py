from django.urls import path
from .views import InstrList, InstrDetail, InstrDashboardView, CourseCreateView, CourseUpdateView, CourseDeleteView, InstructorCourseListView


app_name = 'instructor'

urlpatterns = [
    path('', InstrList.as_view(), name='instrList'), 
    path('dashboard/', InstrDashboardView.as_view(), name='dashboard'),
    path('new_course/', CourseCreateView.as_view(), name='new_course'),
    path('update_course/<int:pk>/', CourseUpdateView.as_view(), name='update_course'),
    path('delete_course/<int:pk>/', CourseDeleteView.as_view(), name='delete_course'),
    path('my_courses/', InstructorCourseListView.as_view(), name='my_courses'),
    path('<int:pk>/', InstrDetail.as_view(), name='instrDetail'),     
    ]