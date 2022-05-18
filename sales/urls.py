from django.urls import re_path
from sales import views

urlpatterns = [
    re_path(r'^create-payment/$', views.create_payment),
]