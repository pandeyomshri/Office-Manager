from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Employee, Role, Department

admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(Department)
