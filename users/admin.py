from django.contrib import admin

# Register your models here.
from users.models import CustomUser, SchoolAdmin, HOD, Staff, Parent, Student

admin.site.register(CustomUser)
admin.site.register(SchoolAdmin)
admin.site.register(HOD)
admin.site.register(Staff)
admin.site.register(Parent)
admin.site.register(Student)