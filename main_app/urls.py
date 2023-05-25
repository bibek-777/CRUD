
from django.urls import path
from main_app import views

urlpatterns = [
    path('', views.home, name='main-app_home'),
    path('home/', views.home, name='main-app_home'),
    path('course/', views.course, name='main-app_course'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deleteall/', views.deleteall, name='deleteall'),
    path('edit/<int:id>', views.edit, name='edit')
]