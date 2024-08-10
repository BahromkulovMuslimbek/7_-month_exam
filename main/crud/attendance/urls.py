from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('attendance-list/', views.listAttendance, name='listAttendance'),
    path('attendance-create/', views.createAttendance, name='createAttendance'),
    path('attendance-detail/<int:id>/', views.detailAttendance, name='detailAttendance'),
    path('attendance-delete/<int:id>/', views.deleteAttendance, name='deleteAttendance'),
    path('attendance-update/<int:id>/', views.updateAttendance, name='updateAttendance'),
]
