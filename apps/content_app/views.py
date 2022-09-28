from django.shortcuts import render
from django.views.generic import TemplateView
from apps.user_app.models import CustomUser
from apps.content_app.models import Content
# Create your views here.

class MainView(TemplateView):
    template_name: str = 'index.html'

class ContentView(TemplateView):
    template_name: str = 'content_app/base.html'

    def get(self, request, *args, **kwargs):
        super().get(self, request, *args, **kwargs)
        content = Content.objects.all()
        return self.render_to_response(context={'content': content})