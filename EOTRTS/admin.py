from django.contrib import admin

from .models import StudentData, TeacherData


class TeacherDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['teacher_id']}),
        (None,    {'fields': ['teacher_name']}),
        ('class', {'fields': ['teacher_class']}),

    ]
    list_display = ('teacher_id', 'teacher_name', 'teacher_class')
    search_fields = ['teacher_id']


class StudentDataAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,    {'fields': ['student_id']}),
        (None,    {'fields': ['student_name']}),
        ('email', {'fields': ['email']}),
        ('class', {'fields': ['class_name']}),

    ]
    list_display = ('student_id', 'student_name', 'email')
    search_fields = ['student_id']


admin.site.register(TeacherData, TeacherDataAdmin)
admin.site.register(StudentData, StudentDataAdmin)

