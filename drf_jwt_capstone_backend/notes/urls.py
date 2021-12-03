from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('note', views.NoteList.as_view()),
    path('note/<int:pk>/', views.NoteDetails.as_view()),
    path('note_type/', views.NoteTypeList.as_view()),
]