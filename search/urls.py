from django.urls import path
from .views import search_results

urlpatterns = [
    path('search/', search_results, name='search_results'),
]
