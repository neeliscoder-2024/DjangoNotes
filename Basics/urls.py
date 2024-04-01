from django.urls import path
from Basics.views import *
app_name='wonders'
urlpatterns=[
    path('basic/',basic,name='basic'),
]