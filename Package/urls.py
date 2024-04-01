from django.urls import path
from Package.views import *
app_name='nothing'
urlpatterns=[
    path('Topic/',Topic,name='Topic'),
]