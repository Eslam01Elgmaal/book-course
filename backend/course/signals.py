# course/signals.py (create if not exists)
from django.db.models.signals import post_save
from django.dispatch import receiver
from moviepy.editor import VideoFileClip
from .models import Lesson


@receiver(post_save, sender=Lesson)
def calculate_video_duration(sender, instance, created, **kwargs):
    if instance.video_file and not instance.video_duration_seconds:
        try:
            clip = VideoFileClip(instance.video_file.path)
            instance.video_duration_seconds = int(clip.duration)
            instance.save(update_fields=['video_duration_seconds'])
            clip.close()
        except Exception as e:
            print(f"Error calculating duration: {e}")