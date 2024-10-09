from django.contrib.auth.models import User
from django.db import models


language_choices = [
    ('Русский', 'Русский'),
    ('Английский', 'Английский'),
    ('Кыргызский', 'Кыргызский'),
    ('Узбекский', 'Узбекский'),
    ('Казахский', 'Казахский'),
    ('Таджикский', 'Таджикский'),
    ('Китайский', 'Китайский'),
]

duration_choices = [
    ('36', '36'),
    ('72', '72'),
]

type_choices = [
    ('file', 'PDF-файл'),
    ('video', 'Видео'),
]

status_choices = [
    ('started', 'Начато'),
    ('finished', 'Завершено'),
]

specialization_choice = [
    ('cardiology', 'Кардиология'),
    ('neurology', 'Неврология'),
    ('orthopedics', 'Ортопедия'),
]

difficulty_choice = [
    ('beginner', 'Начальный'),
    ('intermediate', 'Средний'),
    ('advanced', 'Продвинутый'),
]

credit_type_choice = [
    ('cme', 'CME'),
    ('ce', 'CE'),
    ('other', 'Другое'),
]

lecture_status_choices = [
    ('incompleted', 'Незаконченное'),
    ('completed', 'Законченное'),
]


class Course(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.TextField()
    text = models.TextField(default=" ")
    image = models.ImageField(upload_to='courses/image/')
    language = models.CharField(choices=language_choices, max_length=15)
    duration = models.CharField(choices=duration_choices, max_length=10)
    specialization = models.CharField(max_length=50, choices=specialization_choice, verbose_name="Специализация", default=' ')
    difficulty = models.CharField(max_length=50, choices=difficulty_choice, verbose_name="Сложность", default=difficulty_choice[0])
    credit_type = models.CharField(max_length=50, choices=credit_type_choice, verbose_name="Тип кредитования", default=credit_type_choice[2])
    completion_percent = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=200)
    description = models.TextField()
    sequence_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name} {self.sequence_number}"


class Lecture(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lectures')
    name = models.CharField(max_length=200)
    type = models.CharField(choices=type_choices, max_length=10)
    video = models.FileField(null=True, blank=True)
    pdf = models.FileField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    duration = models.PositiveSmallIntegerField(default=10)
    # status = models.BooleanField()

    def __str__(self):
        return self.name


class UserLecture(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=lecture_status_choices, default='incompleted')

    def __str__(self):
        return f'{self.user} --- {self.lecture}'


class UserCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_choices, max_length=10)

    def __str__(self):
        return f'{self.user} --- {self.course}'

