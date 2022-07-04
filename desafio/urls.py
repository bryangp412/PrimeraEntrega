from django.urls import path, include
from .views import una_vista

urlpatterns = [
    path('', una_vista),
]