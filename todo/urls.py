from django.urls import path
from . import views

urlpatterns = [
    # path('all_questions/', views.get_allQuestions, name='get_allQuestions'),
    # path('allQuestion/', views.AllQuestionsView.as_view(), name='question'),
    path('question/', views.QuestionView.as_view(), name='question_detail'),  # For a specific question
    path('question/<int:id>/', views.QuestionView.as_view(), name='question_detail'),  # For a specific question
    path('choice/', views.ChoiceView.as_view(), name='choice'),
    # path('choices/', views.get_allChoices, name='get_allChoices'),
    # path('todos/', views.get_all_todos, name='get_all_todos'),
]