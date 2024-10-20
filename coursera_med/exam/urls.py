from django.urls import path
from .views import quiz_view, quiz_results


urlpatterns = [
    # path('quiz/', QuizListView.as_view(), name="main-view"),
    path('quiz/<pk>/', quiz_view, name="quiz"),
    path('quiz/<pk>/results', quiz_results, name="quiz_results"),
    # path('quiz/<pk>/data/', quiz_data_view, name="quiz-data"),
    # path('quiz/<pk>/save/', save_quiz_view, name="save-data"),
]
