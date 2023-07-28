from django.contrib import admin
from django.urls import path, include

# If we want to define a path like this, we need to bring a path in
urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
]
