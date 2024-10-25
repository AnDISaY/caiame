from django.db import models
from django.contrib.auth.models import User


documents_status_choices = [
    ('consideration', 'На рассмотрении'),
    ('approved', 'Одобрено'),
    ('denied', 'Отказано'),
]


class UserDocuments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    passport_front = models.ImageField(upload_to='documents/')
    passport_back = models.ImageField(upload_to='documents/')
    diploma = models.ImageField(upload_to='documents/')
    certificate = models.ImageField(upload_to='documents/')
    status = models.CharField(max_length=100, default='consideration', choices=documents_status_choices)

    class Meta:
        verbose_name = 'Документ студента'
        verbose_name_plural = 'Документы студента'

    def __str__(self):
        return f'{self.user} -- {self.status}'
