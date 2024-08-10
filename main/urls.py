from django.urls import path, include
from . import views


urlpatterns = [
   path('', views.index, name='index'),
   path('', include('main.crud.attendance.urls'), name='attendance'),
   path('', include('main.crud.staff.urls'), name='staff'),
   path('login/', views.loginView, name='login'),
   path('logout/', views.logoutView, name='logout'),
   path('profile/', views.profile, name='profile'),
]