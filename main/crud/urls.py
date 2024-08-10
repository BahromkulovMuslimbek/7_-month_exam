from django.urls import path, include

urlpatterns = [
    path('', include('main.crud.staff.urls')),
    
]