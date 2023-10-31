from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import UserManager, AbstractUser
from django.contrib.gis.db import models

from school.models import School


class CustomUserManager(UserManager):
    def _create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = CustomUser(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        assert extra_fields["is_staff"]
        assert extra_fields["is_superuser"]
        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    USER_TYPE = (
        (1, "Staff"),
        (2, "Parent"),
        (3, "Student")
    )
    GENDER = (
        ("M", "Male"),
        ("F", "Female")
    )

    username = None  # Removed username, using email instead
    email = models.EmailField(unique=True)
    user_type = models.CharField(default=1, choices=USER_TYPE, max_length=1)
    gender = models.CharField(max_length=1, choices=GENDER)
    profile_pic = models.ImageField()
    address = models.TextField()
    fcm_token = models.TextField(default="")  # For firebase notifications
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    current_school = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)
    location = models.PointField(null=True, blank=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        verbose_name = 'User Accounts'


class Staff(models.Model):
    user_acc = models.OneToOneField(CustomUser)
    department = models.CharField(max_length=100)
    primary_contact_number = models.CharField(max_length=20)
    secondary_contact_number = models.CharField(max_length=20, null=True, blank=True)
    hire_date = models.DateField()
    current_school = models.ForeignKey(School, on_delete=models.CASCADE)
    schools_taught = models.ManyToManyField(School, related_name='teachers', null=True, blank=True)
    user_type = 1
    educational_level = models.PositiveIntegerField(choices=(
        (1, 'Uneducated'),
        (2, 'Basic School'),
        (3, 'High school'),
        (4, 'Diploma'),
        (5, 'Bachelors'),
        (6, 'Masters'),
        (7, 'PHD or Higher')
    ), default=5)

    class Meta:
        verbose_name_plural = 'Staff'


class SchoolAdmin(models.Model):
    user_acc = models.OneToOneField(CustomUser)
    primary_contact_number = models.CharField(max_length=20)
    secondary_contact_number = models.CharField(max_length=20, null=True, blank=True)
    current_school = models.ForeignKey(School, on_delete=models.PROTECT)
    previous_schools = models.ManyToManyField(School)

    class Meta:
        verbose_name_plural = 'School Administrators'


class HOD(models.Model):
    user_acc = models.OneToOneField(CustomUser)
    department = models.CharField(max_length=100)
    primary_contact_number = models.CharField(max_length=20)
    secondary_contact_number = models.CharField(max_length=20, null=True, blank=True)
    current_school = models.ForeignKey(School, on_delete=models.CASCADE)
    previous_schools = models.ManyToManyField(School)


    class Meta:
        verbose_name_plural = 'School Heads'


class Parent(models.Model):
    user_acc = models.OneToOneField(CustomUser)
    primary_contact_number = models.CharField(max_length=20)
    secondary_contact_number = models.CharField(max_length=20, null=True, blank=True)
    user_type = 2

    class Meta:
        verbose_name_plural = 'Parents'


class Student(models.Model):
    user_acc = models.OneToOneField(CustomUser)
    primary_contact_person = models.ForeignKey(Parent, on_delete=models.PROTECT,
                                               related_name='students_primary_contact')
    grade_level = models.CharField(max_length=2)
    current_school = models.ForeignKey(School, on_delete=models.CASCADE)
    schools_attended = models.ManyToManyField(School, related_name='students')
    user_type = 3

    class Meta:
        verbose_name_plural = 'Students'
