from django.contrib import admin
from django.urls import include, path

urlpatterns = [
	path('', include('mindfulapp.urls')),
    path('admin/', admin.site.urls),
]
