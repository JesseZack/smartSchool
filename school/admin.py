from django.contrib import admin

# Register your models here.
from school.models import Organization, School

admin.site.register(Organization)
admin.site.register(School)