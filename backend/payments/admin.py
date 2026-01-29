# payments/admin.py
from django.contrib import admin
from .models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'student', 'enrollment', 'amount_display', 'currency',
        'status', 'payment_method', 'paid_at', 'created_at'
    )
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = (
        'student__user__first_name', 'student__user__last_name',
        'student__user__email', 'transaction_id', 'enrollment__course__title'
    )
    date_hierarchy = 'paid_at'
    readonly_fields = ('created_at', 'paid_at')
    list_per_page = 20

    def amount_display(self, obj):
        return f"{obj.amount} {obj.currency}"
    amount_display.short_description = "Amount"