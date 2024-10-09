from django.urls import path

from old.views import CoursesListView, create_course_view, course_detail_view, CourseDeleteView, CourseUpdateView, \
    create_module_view, ModuleDetailView, LectureDetailView

urlpatterns = [
    path('courses/', CoursesListView.as_view(), name='courses-list'),
    path('courses/<pk>/', course_detail_view, name='course-detail'),
    path('courses/<pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    path('courses/<pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('create-course/', create_course_view, name='course-create'),
    path('courses/<int:course_pk>/module/<int:pk>/', ModuleDetailView.as_view(), name='module-detail'),
    # path('courses/<pk>/update/', CourseUpdateView.as_view(), name='course-update'),
    # path('courses/<pk>/delete/', CourseDeleteView.as_view(), name='course-delete'),
    path('create-module/', create_module_view, name='module_create'),
    path('learn/<pk>/', LectureDetailView.as_view(), name='lecture-detail'),

]
