from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="index") #google.com/databes_app
]
