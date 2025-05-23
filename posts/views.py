from django.shortcuts import render
from .models import post
from django.views.generic import ListView
from django.views import View
# Create your views here.

class postListView(ListView):
    model = post
    template_name = 'home.html'
    paginate_by = 10
    context_object_name = 'abc'

class Custom404View(View):
    def get(self, request, *args, **kwargs):
        return render(request, '404.html', status=404)
