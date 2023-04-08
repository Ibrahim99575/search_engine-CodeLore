from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', include('search.urls')),
    path('', lambda request: redirect('search_results'), name='root'),
    path('search/', lambda request: redirect('search_results'), name='root'),
    path('admin/', admin.site.urls),
]

