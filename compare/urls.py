from django.urls import path
from . import views

urlpatterns = [
    path('compare/', views.compare_faces),
    path('<str:folder>/<str:filename>', views.serve_known_face),
]