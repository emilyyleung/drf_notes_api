from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/', views.notesList, name="notes"),
    path('notes/<str:pk>', views.noteDetail, name="note"),
]