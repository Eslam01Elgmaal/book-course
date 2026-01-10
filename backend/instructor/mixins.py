from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

class InstructorRequiredMixin(LoginRequiredMixin):

    def dispatch(self, request, *args, **kwargs):
      
        if not hasattr(request.user, 'instructor'):
            raise PermissionDenied  
        return super().dispatch(request, *args, **kwargs)
