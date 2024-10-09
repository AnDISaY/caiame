from django.urls import path
from .views import QuizListView, quiz_view, quiz_data_view, save_quiz_view

app_name = "quizes"

urlpatterns = [
    path('quiz/', QuizListView.as_view(), name="main-view"),
    path('quiz/<pk>/', quiz_view, name="quiz"),
    path('quiz/<pk>/data/', quiz_data_view, name="quiz-data"),
    path('quiz/<pk>/save/', save_quiz_view, name="save-data"),
]
