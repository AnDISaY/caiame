from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from .forms import CourseForm, ModuleForm, LectureForm, UserCourseForm
from .models import Course, Module, Lecture, UserCourse, UserLecture
from main.models import UserDocuments
from exam.models import Result


def status_check(user):
    user_documents = UserDocuments.objects.get(user=user)
    status = False
    if user_documents.status == 'approved':
        status = True
    return status


class CoursesListView(ListView):
    model = Course
    template_name = 'courses/courses/courses_list.html'


# class CourseDetailView(DetailView):
#     model = Course
#     form_class = UserCourseForm()
#     template_name = 'courses/courses/course_detail.html'
#     extra_context = {"form": form_class}
#
#     def get(self, request, *args, **kwargs):
#         print(request.method)
#         obj = Course.objects.get(pk=kwargs['pk'])
#         return render(request, 'courses/courses/course_detail.html', {'object': obj})


def course_detail_view(request, pk):
    object = Course.objects.get(pk=pk)
    relation_is_exists = False

    quizes_queryset = object.quizes.filter(course=object)
    quizes = list(object.quizes.filter(course=object).values())

    for index in range(0, len(quizes)):
        try:
            result = Result.objects.get(quiz=quizes_queryset[index], user=request.user)
        except:
            result = None
        quizes[index]['result'] = result


    if request.user.is_authenticated:
        if UserCourse.objects.filter(course=object, user=request.user):
            relation_is_exists = True
        if request.method == 'POST' and not relation_is_exists:
            us = UserCourse.objects.create(course=object, user=request.user, status='started')
            for module in us.course.modules.all():
                for lecture in module.lectures.all():
                    UserLecture.objects.create(lecture=lecture, module=module, user=request.user)
            return render(request, 'courses/course.html', {'object': object,
                                                                          'relation_is_exists': relation_is_exists, 'user': request.user.is_authenticated, 'documents_status': status_check(request.user)})
    return render(request, 'courses/course.html', {'object': object,
                                                                  'relation_is_exists': relation_is_exists, 'user': request.user.is_authenticated, 'quizes': quizes, 'documents_status': status_check(request.user)})


def create_course_view(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    else:
        form = CourseForm()
    return render(request, 'courses/courses/create_course.html', {'form': form})


# class CourseCreateView(CreateView):
#     model = Course
#     form_class = CourseForm
#     template_name = 'courses/courses/create_course.html'


class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'courses/courses/create_module.html'
    fields = ['name', 'description', 'image', 'duration', 'language', ]
    success_url = '/courses'


class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'courses/courses/delete_course.html'
    success_url = '/courses'


# class ModuleDetailView(DetailView):
#     model = Module
#     template_name = 'courses/module/module_detail.html'


def module_detail_view(request, pk, course_pk):
    if not status_check(request.user):
        return redirect('/home')
    module = Module.objects.get(id=pk)
    lectures = UserLecture.objects.filter(module=module)
    return render(request, 'courses/module.html', {'module': module, 'user': request.user.is_authenticated, 'lectures': lectures,})


def create_module_view(request):
    if request.method == 'POST':
        form = ModuleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    else:
        form = ModuleForm()
    return render(request, 'courses/module/create_module.html', {'form': form})


class ModuleUpdateView(UpdateView):
    model = Module
    template_name = 'courses/module/create_module.html'
    fields = ['name', 'description', 'sequence_number', ]
    success_url = '/courses'


class ModuleDeleteView(DeleteView):
    model = Module
    template_name = 'courses/module/delete_module.html'
    success_url = '/courses'


# class LectureDetailView(DetailView):
#     model = Lecture
#     template_name = 'courses/lecture/lecture_detail.html'

def lecture_detail_view(request, pk):
    if not status_check(request.user):
        return redirect('/home')
    lecture = Lecture.objects.get(pk=pk)
    user_lecture = UserLecture.objects.get(lecture=lecture)
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        user_lecture.status = 'completed'
        user_lecture.save()
        return render(request, 'courses/lecture.html', {'object': lecture, 'user': request.user.is_authenticated, 'user_lecture': user_lecture,})
    return render(request, 'courses/lecture.html', {'object': lecture, 'user': request.user.is_authenticated, 'user_lecture': user_lecture,})


def create_lecture_view(request):
    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/courses')
    else:
        form = LectureForm()
    return render(request, 'courses/lecture/create_lecture.html', {'form': form})


class LectureUpdateView(UpdateView):
    model = Lecture
    template_name = 'courses/lecture/create_lecture.html'
    fields = ['name', 'type', 'video', 'text', ]
    success_url = '/courses'


class LectureDeleteView(DeleteView):
    model = Lecture
    template_name = 'courses/lecture/delete_lecture.html'
    success_url = '/courses'
