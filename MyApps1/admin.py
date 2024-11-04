from django.contrib import admin
from MyApps1.models import Students


# Register your models here.

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','dept','marks']

admin.site.register(Students,StudentsAdmin)
