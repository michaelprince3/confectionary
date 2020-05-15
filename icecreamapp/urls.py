from django.urls import path
from icecreamapp import views
from .views import *

app_name = "icecreamapp"

urlpatterns = [
    path('', home, name='home'),
    path('form', form, name='form'),
    path('detail/<int:variety_id>/', detail, name='detail')
]
