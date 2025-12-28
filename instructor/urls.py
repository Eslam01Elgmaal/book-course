from django.urls import path
from .views import InstrList, InstrDetail, InstrDashboardView


app_name = 'instructor'

urlpatterns = [
    path('', InstrList.as_view(), name='instrList'), 
    path('dashboard/', InstrDashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', InstrDetail.as_view(), name='instrDetail'), 

    
    
    
    ]