from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView

from coursera_med.courses.forms import CourseForm, ModuleForm, LectureForm, UserCourseForm
from coursera_med.courses.models import Course, Module, Lecture, UserCourse


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
    obj = Course.objects.get(pk=pk)
    relation_is_exists = False
    if request.user.is_authenticated:
        if UserCourse.objects.filter(course=obj, user=request.user):
            relation_is_exists = True
        if request.method == 'POST' and not relation_is_exists:
            UserCourse.objects.create(course=obj, user=request.user, status='started')
            return render(request, 'courses/courses/course_detail.html', {'object': obj,
                                                                          'relation_is_exists': relation_is_exists})
    return render(request, 'courses/courses/course_detail.html', {'object': obj,
                                                                  'relation_is_exists': relation_is_exists})


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


class ModuleDetailView(DetailView):
    model = Module
    template_name = 'courses/module/module_detail.html'


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


class LectureDetailView(DetailView):
    model = Lecture
    template_name = 'courses/lecture/lecture_detail.html'


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
