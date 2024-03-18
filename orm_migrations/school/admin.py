from django.contrib import admin
from .models import Student
from .models import Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'group')
    list_filter = ('group',)
    search_fields = ('name', 'group')



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject')
    list_filter = ('subject',)
    search_fields = ('name', 'subject')

