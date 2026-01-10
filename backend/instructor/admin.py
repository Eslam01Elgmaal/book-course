from django.contrib import admin
from .models import Instructor
# Register your models here.


@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name','email' , 'date_joined') 