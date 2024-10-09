from django.db import models
from django.contrib.auth.models import User


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    number_of_questions = models.PositiveSmallIntegerField()
    time = models.SmallIntegerField()
    practice = models.BooleanField()
    required_score_to_pass = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_questions(self):
        return self.questions.all()

    class Meta:
        verbose_name_plural = "Quizes"


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answers.all()


class Answer(models.Model):
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answers")

    def __str__(self):
        return str(f"{self.text}, {self.is_correct}")


class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.score)
