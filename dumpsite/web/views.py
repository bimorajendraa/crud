from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'base.html'

    def get(self, request):
        return render(request, self.template_name)