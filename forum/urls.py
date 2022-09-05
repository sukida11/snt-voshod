from django.urls import path

from .views import *

app_name = 'forum'

# 3 url для приложения forum
urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('create_question/', CreateQuestionView.as_view(), name='create_question'),
	path('<int:pk>/', CheckQuestionView.as_view(), name='check_question'),
]
