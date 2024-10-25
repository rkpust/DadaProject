from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('submit-form', views.submit_form, name='submit-form'),
]