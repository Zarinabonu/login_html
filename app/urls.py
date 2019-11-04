from django.urls import path

from app import views

urlpatterns = [
    path('', views.TemplateCall.as_view(), name='base'),
]