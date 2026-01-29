# payments/models.py
from django.db import models


class Payment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    )

    METHOD_CHOICES = (
        ('stripe', 'Stripe'),
        ('paypal', 'PayPal'),
        ('manual', 'Manual / Bank Transfer'),
        ('other', 'Other'),
    )

    enrollment = models.ForeignKey('enrollments.Enrollment', on_delete=models.PROTECT, related_name='payments')
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    payment_method = models.CharField(max_length=30, choices=METHOD_CHOICES, default='manual')
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)
    proof_file = models.FileField(upload_to='payment_proofs/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment #{self.id} – {self.student} – {self.amount} {self.currency}"