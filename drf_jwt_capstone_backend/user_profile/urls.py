from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.Profile.as_view()),
    
]