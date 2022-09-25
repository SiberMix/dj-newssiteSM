from django.urls import include, path
from .views import index, get_category

urlpatterns = [
    path('', index),
    path('category/<int:category_number>/', get_category),
]