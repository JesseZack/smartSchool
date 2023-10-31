from django.db import models

# Create your models here.
from school.models import School
from users.models import Staff, Student


class AcademicYear(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f'{self.start_date} to {self.end_date}'


class Course(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=120)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE,)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name}'


class SchoolClass(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50, unique=True)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.SET_NULL, null=True, blank=True)
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(Student, related_name='enrolled_classes')
    subjects = models.ManyToManyField(Subject, related_name='classes_taught')
    description = models.TextField(blank=True)


class TimeTable(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)

    WEEKDAY_CHOICES = (
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    )
    period = models.PositiveSmallIntegerField()
    weekday = models.CharField(max_length=3, choices=WEEKDAY_CHOICES)
    is_holiday = models.BooleanField(default=False)
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_weekday_display()} - Period {self.period}: {self.subject}"


class AttendanceReport(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attendance = models.ForeignKey(TimeTable, on_delete=models.CASCADE)
    is_present = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StaffAttendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.DO_NOTHING)
    date = models.DateField()
    is_present = models.BooleanField(default=False)


