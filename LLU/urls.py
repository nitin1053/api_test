from django.urls import path,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from LLU.views import *
from rest_framework import status
import csv
import json
from io import TextIOWrapper

urlpatterns=[
    path('',Hello.as_view()),
    path('training_model/<str:train>',TrainingClass.as_view()),
    path('csvjson',csvreader.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)