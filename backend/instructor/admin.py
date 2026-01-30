# instructor/admin.py
from django.contrib import admin
from .models import Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'date_joined')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('date_joined',)