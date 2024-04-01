from django.urls import path
from Framework.views import *
app_name='anything'
urlpatterns=[
    path('Topics/',Topics,name='Topics'),
]