from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.models import User

from django.http import JsonResponse
from django.core.serializers import serialize
import json

from .forms import RegisterForm, LoginForm, UserDocumentsForm
from courses.forms import CourseFilterForm
from courses.models import UserCourse, Lecture, Course, UserLecture
from .models import UserDocuments



def logout_required(
    function=None, redirect_field_name="next", login_url=None
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def home(request):
    user = request.user.is_authenticated
    courses = Course.objects.all()
    form = CourseFilterForm()

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        specialization = request.POST['specialization']
        difficulty = request.POST['difficulty']
        credit_type = request.POST['credit_type']
        filter_courses = courses.filter(specialization__exact=specialization, difficulty__exact=difficulty, credit_type__exact=credit_type)
        serialized_data = serialize("json", filter_courses)
        serialized_data = json.loads(serialized_data)
        return JsonResponse({"courses": serialized_data})

    return render(request, 'home.html', {'courses': courses, 'user': user, "form": form, })


@logout_required(login_url='/profile')
def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/success')
    else:
        form = RegisterForm()
    return render(request, 'account/signup.html', {"form": form, 'user': request.user.is_authenticated,})


def success(request):
    if not request.session.has_key('has_reffered') or request.session["has_reffered"] == True:
        return render(request, 'account/success.html', {'user': request.user,})
    return redirect('/home')


@logout_required(login_url='/home')
def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect('/profile')
        else:
            return render(request, 'account/login.html', {"form": form, "error": "Неверно введены имя пользователя или пароль", 'user': request.user.is_authenticated,})
    return render(request, 'account/login.html', {"form": form, 'user': request.user.is_authenticated,})


@login_required(login_url='/login')
def profile(request):
    user_courses = UserCourse.objects.filter(user=request.user)
    try:
        user_documents = UserDocuments.objects.get(user=request.user)
    except:
        user_documents = None

    context = {'user_courses': user_courses, 'user': request.user, "user_documents": user_documents}
    try:
        context['documents_message'] = request.session.pop('documents_message')
    except:
        context['documents_message'] = None
    
    lectures_quantity = 0
    completed_lectures_quantity = 0
    if user_courses:
        for course in user_courses:
            for module in course.course.modules.all():
                lectures_quantity += module.lectures.all().count()
                for lecture in UserLecture.objects.filter(module=module):
                    if lecture.status == 'completed':
                        completed_lectures_quantity += 1
            if completed_lectures_quantity != 0:
                course.completion_percent = round((completed_lectures_quantity/lectures_quantity) * 100)
            else:
                course.completion_percent = 0
        context['completion_percent'] = course.completion_percent
    
    return render(request, 'account/profile.html', context=context)


def add_documents(request):
    if request.method == 'POST':
        form = UserDocumentsForm(request.POST, request.FILES, instance=UserDocuments.objects.get(user=request.user))
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            request.session['documents_message'] = 'Данные успешно сохранены. Дождитесь проверки документов'
            return redirect('/profile')
    else:
        form = UserDocumentsForm()
    return render(request, 'account/add_documents.html', {"form": form, "user": request.user})
