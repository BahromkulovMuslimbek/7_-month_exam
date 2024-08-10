from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from main import models


@login_required(login_url='login')
def listStaff(request):
    queryset = models.Staff.objects.all()
    context = {'queryset': queryset}
    return render(request, 'crud/staff/list.html', context)

@login_required(login_url='login')
def detailStaff(request, id):
    queryset = models.Staff.objects.get(id=id)
    context = {'queryset': queryset}
    return render(request, 'crud/staff/detail.html', context)

@login_required(login_url='login')
def createStaff(request):
    if request.method == 'POST':
        staff = models.Staff.objects.create(
            username=request.POST['username'],
            phone=request.POST['phone'],
            job_title=request.POST['job_title'],
            adress=request.POST['adress']
        )
        return redirect('staff:listStaff')
    return render(request, 'crud/staff/create.html')

@login_required(login_url='login')
def deleteStaff(request, id):
    models.Staff.objects.get(id=id).delete()
    return redirect('staff:listStaff')

@login_required(login_url='login')
def updateStaff(request, id):
    data = models.Staff.objects.get(id=id)
    if request.method == 'POST':
        data.username = request.POST['username']
        data.phone = request.POST['phone']
        data.job_title = request.POST['job_title']
        data.adress = request.POST['adress']
        data.save()
        return redirect('staff:listStaff')
    return render(request, 'crud/staff/update.html', {'data': data})