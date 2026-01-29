# enrollments/models.py
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Enrollment(models.Model):
    student = models.ForeignKey('student.Student', on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey('course.Course', on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    progress = models.FloatField(
        default=0.0,
        validators=[MinValueValidator(0.0), MaxValueValidator(100.0)],
        help_text="0.0 to 100.0 – overall course progress"
    )
    last_activity = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['student', 'course'], name='unique_enrollment')]
        ordering = ['-enrolled_at']

    def __str__(self):
        return f"{self.student} → {self.course.title}"

    @property
    def is_completed(self):
        return self.completed or self.progress >= 99.9


class LessonProgress(models.Model):
    """
    Per-lesson progress for accurate tracking
    """
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE, related_name='lesson_progress')
    lesson = models.ForeignKey('course.Lesson', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    watch_time_seconds = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = [['enrollment', 'lesson']]
        ordering = ['lesson__order']

    def __str__(self):
        return f"{self.enrollment} – {self.lesson.title}"