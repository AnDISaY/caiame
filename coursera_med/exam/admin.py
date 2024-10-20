from django.contrib import admin
from .models import Result, Quiz, Question, Answer, ResultAnswers


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    exclude = ['correct_count']


class QuestionLinkInline(admin.TabularInline):
    model = Question
    exclude = ['correct_count']
    show_change_link = True


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionLinkInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(ResultAnswers)
