from django.shortcuts import render, redirect
from datetime import datetime
from main import models
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def listAttendance(request):
    queryset = models.Attendance.objects.all()
    context = {'queryset': queryset}
    return render(request, 'crud/attendance/list.html', context)

@login_required(login_url='login')
def detailAttendance(request, id):
    queryset = models.Attendance.objects.get(id=id)
    context = {'queryset': queryset}
    return render(request, 'crud/attendance/detail.html', context)

@login_required(login_url='login')
def createAttendance(request):
    if request.method == 'POST':
        staff = models.Staff.objects.get(id=request.POST['staff_id'])
        date = request.POST['date']
        time = request.POST['time']
        date_time = datetime(int(date[:4]), int(date[5:7]), int(date[8:]), int(time[:2]), int(time[3:]))
        attendance = models.Attendance.objects.create(
            staff=staff,
            status=request.POST['status'],
            date_time=date_time

        )
        return redirect('attendance:listAttendance')
    staffs = models.Staff.objects.all()
    return render(request, 'crud/attendance/create.html', {'staffs': staffs})

@login_required(login_url='login')
def deleteAttendance(request, id):
    models.Attendance.objects.get(id=id).delete()
    return redirect('attendance:listAttendance')

@login_required(login_url='login')
def updateAttendance(request, id):
    attendance = models.Attendance.objects.get(id=id)
    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')
        date_time = datetime(int(date[:4]), int(date[5:7]), int(date[8:]), int(time[:2]), int(time[3:]))
        attendance.status = request.POST['status']
        attendance.date_time = date_time
        attendance.save()
        return redirect('attendance:listAttendance')
    return render(request, 'crud/attendance/update.html', {'attendance':attendance})