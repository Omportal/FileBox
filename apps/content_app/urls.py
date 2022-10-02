from django.urls import path
from .views import MainView, ContentView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('content', ContentView.as_view(), name='content'),
]