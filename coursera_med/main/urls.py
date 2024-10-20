from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signup/', views.sign_up, name='signup'),
    path('success/', views.success, name='success'),
    path('login/', views.sign_in, name='login'),
    # path('reset_password/', views.reset_password, name='reset_password'),
    path('profile/', views.profile, name='profile'),
    path('profile/add_documents/', views.add_documents, name='add_documents'),
]
