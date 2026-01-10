from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import InstructorRequiredMixin
from django.urls import reverse
from course.models import Course 
from django.shortcuts import redirect
from .models import Instructor


class InstrDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'instructor/dashboard.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context["instructor"] = Instructor.objects.get(user=self.request.user)
        return context

class InstrList(LoginRequiredMixin, ListView):
    model = Instructor
    template_name = 'instructor/instructor_list.html'
    context_object_name = 'instructors'


class InstrDetail(LoginRequiredMixin, DetailView):
    model = Instructor
    template_name = 'instructor/instructor_detail.html'
    context_object_name = 'instructor'


class CourseCreateView(InstructorRequiredMixin, CreateView):
    model = Course
    fields = ['title', 'description', 'price']
    template_name = 'instructor/course_create.html'

    def form_valid(self, form):
        form.instance.instructor = self.request.user.instructor
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('instructor:dashboard')




class CourseUpdateView(InstructorRequiredMixin, UpdateView):
    model = Course
    fields = ['title', 'description', 'price']
    template_name = 'instructor/course_edit.html'

    def get_success_url(self):
        return reverse('instructor:dashboard')




class CourseDeleteView(InstructorRequiredMixin, DeleteView):
    model = Course
    template_name = 'instructor/course_delete.html'

    def get_success_url(self):
        return reverse('instructor:dashboard')



class InstructorCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'instructor/instructor_courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(instructor=self.request.user.instructor)
