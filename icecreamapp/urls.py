from django.urls import path
from icecreamapp import views
from .views import *

app_name = "icecreamapp"

urlpatterns = [
    path('', home, name='home'),
]
