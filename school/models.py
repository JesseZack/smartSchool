from django.contrib.gis.db import models


class Organization(models.Model):
    name = models.CharField(max_length=100)
    headquarters = models.CharField(max_length=100)
    type = models.CharField(max_length=1, choices=(('I', 'Individual'), ('O', 'Organization')), )

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    address = models.TextField()
    established_by = models.ForeignKey(Organization, on_delete=models.PROTECT)
    website = models.URLField(max_length=200, blank=True, null=True, help_text="The school's website URL")
    contact_number = models.CharField(max_length=20, blank=True, null=True, help_text="Contact number for the school")
    founded_date = models.DateField(blank=True, null=True, help_text="The date the school was founded")
    description = models.TextField(blank=True, help_text="A brief description of the school")
    logo = models.ImageField(upload_to='school_logos/', blank=True, null=True, help_text="School logo image")
    geolocation = models.PointField()

    def __str__(self):
        return f'{self.name} - {self.branch}'

