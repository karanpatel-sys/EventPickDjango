from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('compare.urls')),  # 👈 compare app ke URLs yaha include karo
]