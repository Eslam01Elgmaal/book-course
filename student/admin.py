# student/admin.py
from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'phone_number', 'user_email', 'user_username')
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__username', 'phone_number')
    list_filter = ('user__is_active',)

    def student_name(self, obj):
        return obj.__str__()  # uses your improved __str__
    student_name.short_description = "Name"

    def user_email(self, obj):
        return obj.user.email or "-"
    user_email.short_description = "Email"

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = "Username"