from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListaTareasApiView, TareasApiView


urlpatterns = [
    path("tareas/", ListaTareasApiView.as_view()),
    path("tareas/<int:pk>", TareasApiView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)