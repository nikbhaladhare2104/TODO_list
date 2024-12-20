from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.QuestionView.as_view(), name='question_detail'),  # For a specific question
    path('question/<int:id>/', views.QuestionView.as_view(), name='question_detail'),  # For a specific question
    path('choice/', views.ChoiceView.as_view(), name='choice'),
    path('todos/', views.TodoView.as_view(), name='todos'),
]