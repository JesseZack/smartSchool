from django.core.exceptions import ValidationError
from django.db import models

from school.models import School
from users.models import Student


class Hostel(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.TextField()
    capacity = models.PositiveIntegerField()
    logo = models.ImageField(null=True, blank=True)

    class Meta:
        unique_together = ('school', 'name')

    def __str__(self):
        return f'{self.name}'


class Room(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10)
    capacity = models.PositiveIntegerField()
    vacant_beds = models.PositiveIntegerField()

    def __str__(self):
        return f"Room {self.room_number}, {self.hostel}"


class StudentAccommodation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()

    class Meta:
        verbose_name_plural = 'Student Accommodation'
        unique_together = ('student', 'room')

    def __str__(self):
        return f"{self.student} - {self.room} ({self.check_in_date} to {self.check_out_date})"

    def save(self, *args, **kwargs):
        if self.room.vacant_beds <= 0:
            raise ValidationError(f'The room {self.room} is already at full occupancy')
        self.room.vacant_beds -= 1
        self.room.save()
        super().save(*args, **kwargs)


class RoomAllocation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    allocation_date = models.DateField()

    def __str__(self):
        return f"{self.student} allocated to {self.room} on {self.allocation_date}"


class MaintenanceRequest(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    request_date = models.DateField()
    description = models.TextField()
    status = models.PositiveIntegerField(choices=(
        (1, 'Pending'),
        (2, 'Completed')
    ), default=1)

    def __str__(self):
        return f"Request by {self.student} in {self.room}: {self.description[:20]}"
