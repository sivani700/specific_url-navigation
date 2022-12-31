from django.urls import path
from app2.views import *
app_name='sivani'
urlpatterns=[
    path('a2_second/',a2_second,name='a2_second'),
]
