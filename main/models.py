from django.db import models


class Staff(models.Model):
    username = models.CharField(max_length=255, null=True)
    phone = models.IntegerField(null=True)
    job_title = models.CharField(max_length=255, null=True)
    adress = models.TextField(null=True)

    def __str__(self):
        return self.username if self.username else "Empty"


class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')], null=True)
    date_time = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.staff.username} - {self.date_time} - {self.status}"
    

class Profile(models.Model):
    full_name = models.CharField(max_length=255, null=True)
    img = models.ImageField(null=True)
    phone = models.IntegerField(null=True)
    adress = models.TextField(null=True)

    def __str__(self):
        return self.full_name if self.full_name else "Empty"