from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('signup.html/', views.signup),
    path('login/', views.login),
    path('recoveryEmail/', views.recoveryEmail),
    path('recoveryEmail/confirmCode', views.confirmCode),
    path('recoveryEmail/newPassword/', views.newPassword),
    path('studentAdminPanel/', views.studentAdminPanel),
    path('studentAdminPanel/calenderstd/', views.calenderstd),
    path('adminLogin/', views.adminLogin),
    path('adminDashboard/', views.adminDashboard),

    path('manageAdmissions/', views.manageAdmissions),


    path('manageStudent/', views.manageStudent),

    path('manageVehicels/', views.manageVehicels),
    
    path('manageInstructor/', views.manageInstructor),

    path('manageCourses/', views.manageCourses),
# path('login/studentAdminPanel/calenderstd/', views.calenderstd),

]