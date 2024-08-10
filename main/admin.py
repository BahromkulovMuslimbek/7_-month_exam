from django.contrib import admin
from . import models


admin.site.register(models.Staff)
admin.site.register(models.Attendance)
admin.site.register(models.Profile)