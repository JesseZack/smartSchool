from django.contrib import admin

# Register your models here.
from academics.models import AcademicYear, Course, Subject, SchoolClass, TimeTable, AttendanceReport

admin.site.register(AcademicYear)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(SchoolClass)
admin.site.register(TimeTable)
admin.site.register(AttendanceReport)