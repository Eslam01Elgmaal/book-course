from rest_framework import serializers
from .models import Payment
from enrollments.serializers import EnrollmentSerializer


class PaymentSerializer(serializers.ModelSerializer):
    enrollment_info = serializers.CharField(source='enrollment.__str__', read_only=True)
    enrollment = EnrollmentSerializer(read_only=True, required=False)

    class Meta:
        model = Payment
        fields = [
            'id', 'enrollment', 'enrollment_info', 'student', 'amount',
            'currency', 'payment_method', 'transaction_id', 'status',
            'created_at', 'paid_at', 'proof_file'
        ]
        read_only_fields = ['created_at', 'paid_at']