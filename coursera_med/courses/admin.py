from django.contrib import admin

from .models import Lecture, Module, Course, UserCourse, UserLecture
from exam.models import Quiz


class LectureInline(admin.TabularInline):
    model = Lecture


class ModuleAdmin(admin.ModelAdmin):
    inlines = [LectureInline]


class ModuleLinkInline(admin.TabularInline):
    model = Module
    show_change_link = True


class QuizInline(admin.TabularInline):
    model = Quiz
    show_change_link = True


class CourseAdmin(admin.ModelAdmin):
    inlines = [ModuleLinkInline, QuizInline]
    exclude = ['completion_percent']


admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lecture)
admin.site.register(UserCourse)
admin.site.register(UserLecture)
