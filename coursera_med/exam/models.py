from django.db import models
from django.contrib.auth.models import User

from courses.models import Course


quiz_status_choices = [
    ('incompleted', 'Незаконченное'),
    ('completed', 'Законченное'),
]


class Quiz(models.Model):
    course =  models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizes')
    name = models.CharField(max_length=200)
    required_score_to_pass = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        return self.questions.all()

    class Meta:
        verbose_name_plural = "Quizes"


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    text = models.CharField(max_length=200)
    correct_count = models.PositiveSmallIntegerField(null=True, blank=True)
    score = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()

    def __str__(self):
        return str(f"{self.text}, {self.is_correct}")


class Result(models.Model):
    course =  models.ForeignKey(Course, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='results')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=quiz_status_choices, default='incompleted')
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.score)
    

class ResultAnswers(models.Model):
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='answers')
    answer_dict = models.JSONField()
