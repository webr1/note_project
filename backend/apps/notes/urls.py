
from django.urls import path
from .models import Note
from .views import NoteList ,NoteDetail


app_name = 'notes'
urlpatterns = [
    path('notes/', NoteList.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetail.as_view(), name='note-detail'),
]