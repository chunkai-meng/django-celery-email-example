from django.urls import path
from .views import celery_email

urlpatterns = [
    path('single/', celery_email),
]
