from django.urls import path
from .views import *

urlpatterns = [
    path("",index),
    path("course/<int:pk>",coure_detail,name='c'),
    path("classwork",classwork),
    path("people",people),
    path("grades",grades),
    path("lecturer",lecturer),
    path("lprofile/<int:pk>",lecturer_profile,name='lprof'),
    path("student",student),
    path("sprofile/<int:pk>",student_profile,name='sprof'),
]