from django.urls import path
from .views import InstrList, InstrDetail


app_name = 'instructor'

urlpatterns = [
    path('', InstrList.as_view(), name='InstrList'), 

    path('<int:pk>/', InstrDetail.as_view(), name='InstrDetail'),  ]