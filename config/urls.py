# config/urls.py

# Django modules

from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # post
    path('', include('app.post.urls', namespace='post')),

    # admin
    path('admin/', admin.site.urls),
]
