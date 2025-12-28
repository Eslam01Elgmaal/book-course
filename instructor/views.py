from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
#from course.models import fun_name #fun name
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

"""
class CourseCreateView(InstructorRequiredMixin, CreateView):
    def post(self, request):
        instructor = request.user.instructor

        course = what_name(instructor=instructor,  #fun name
        titel=request.POST["titel"],description=request.POST["description"],
        price=request.POST['price'])

        return redirect("instructor:dashboard")
"""