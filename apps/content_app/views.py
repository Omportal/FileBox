import os
from pprint import pprint
import sys
from xmlrpc.client import ResponseError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, View
from apps.user_app.models import CustomUser
from apps.content_app.models import Content
from .forms import ContentForm
# Create your views here.

class MainView(TemplateView):
    template_name: str = 'index.html'

class ContentView(FormView):
    form_class = ContentForm
    success_url = 'content'
    template_name: str = 'content_app/base.html'

    def get(self, request, *args, **kwargs):
        content = Content.objects.all()
        return render(request, self.template_name, {'content': content})
    
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                Content.objects.create(user=request.user, upload=f, name=f.name)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)