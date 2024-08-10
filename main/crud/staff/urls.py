from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('staff-list/', views.listStaff, name='listStaff'),
    path('staff-create/', views.createStaff, name='createStaff'),
    path('staff-detail/<int:id>/', views.detailStaff, name='detailStaff'),
    path('staff-delete/<int:id>/', views.deleteStaff, name='deleteStaff'),
    path('staff-update/<int:id>/', views.updateStaff, name='updateStaff'),
]