from django.contrib import admin

from .models import Lecture, Module, Course, UserCourse, UserLecture

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lecture)
admin.site.register(UserCourse)
admin.site.register(UserLecture)
