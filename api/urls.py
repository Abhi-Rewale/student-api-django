
from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('students/',views.show),
    path('students/getbyid/<int:id>/',views.get_student),
    path('students/search/<str:name>/', views.search_by_name),  
    path('students/add/',views.add_student),
    path('students/edit/<int:id>/',views.edit_student),
    path('students/delete/<int:id>/',views.delete_student),
    path('register/', views.register_user),
    path('login/', views.login_user),

]
