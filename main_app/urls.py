
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='main-app_home'),
    path('home/', views.home, name='main-app_home'),
    path('course/', views.course, name='main-app_course')
]