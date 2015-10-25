from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
from lindy.models import Teacher


class TeacherAdmin(ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
