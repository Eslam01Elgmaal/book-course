# course/models.py
from django.db import models
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon name, e.g. fa-code")

    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    instructor = models.ForeignKey('instructor.Instructor', on_delete=models.PROTECT, related_name='created_courses')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    description = models.TextField()
    what_you_will_learn = models.TextField(blank=True, help_text="One point per line – what student gains")
    requirements = models.TextField(blank=True, help_text="One point per line – what student needs to know")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    language = models.CharField(max_length=50, default="English")
    level = models.CharField(
        max_length=20,
        choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')],
        default='beginner'
    )
    thumbnail = models.ImageField(upload_to='course_thumbnails/', blank=True, null=True)
    trailer_url = models.URLField(blank=True, null=True, help_text="Preview video – YouTube/Vimeo")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.title)
            slug = base
            counter = 1
            while Course.objects.filter(slug=slug).exists():
                slug = f"{base}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    @property
    def current_price(self):
        return self.discount_price if self.discount_price else self.price

    @property
    def has_discount(self):
        return bool(self.discount_price and self.discount_price < self.price)


class Module(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField(blank=True)
    is_free_preview = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'title']
        unique_together = [['course', 'order']]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.title} – {self.title}"


class Lesson(models.Model):
    TYPE_CHOICES = (
        ('video', 'Video'),
        ('article', 'Article / Text'),
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
        ('download', 'Downloadable Resource'),
        ('other', 'Other'),
    )

    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, blank=True)
    order = models.PositiveIntegerField(default=0)
    lesson_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='video')
    duration_minutes = models.PositiveIntegerField(null=True, blank=True, help_text="Duration in minutes (video)")
    content = models.TextField(blank=True)  # rich text / markdown for articles
    # video_url = models.URLField(blank=True, null=True)
    # Video options (choose ONE method per lesson)
    video_url = models.URLField(blank=True, null=True, help_text="YouTube/Vimeo embed URL (for long videos)")
    video_file = models.FileField(
        upload_to='lesson_videos/%Y/%m/%d/',
        blank=True, 
        null=True,
        help_text="Upload short video (MP4, max 500MB, under 15 min recommended)"
    )
    external_url = models.URLField(blank=True, null=True, help_text="External resource link")
    file = models.FileField(upload_to='lesson_files/', blank=True, null=True)
    is_preview = models.BooleanField(default=False)

    class Meta:
        ordering = ['order', 'title']
        unique_together = [['module', 'order']]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.module.title} – {self.title}"