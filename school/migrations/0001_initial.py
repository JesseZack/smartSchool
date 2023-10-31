# Generated by Django 4.2.5 on 2023-10-06 18:23

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("headquarters", models.CharField(max_length=100)),
                (
                    "type",
                    models.CharField(
                        choices=[("I", "Individual"), ("O", "Organization")],
                        max_length=1,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("branch", models.CharField(max_length=50)),
                ("address", models.TextField()),
                (
                    "website",
                    models.URLField(
                        blank=True, help_text="The school's website URL", null=True
                    ),
                ),
                (
                    "contact_number",
                    models.CharField(
                        blank=True,
                        help_text="Contact number for the school",
                        max_length=20,
                        null=True,
                    ),
                ),
                (
                    "founded_date",
                    models.DateField(
                        blank=True,
                        help_text="The date the school was founded",
                        null=True,
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, help_text="A brief description of the school"
                    ),
                ),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        help_text="School logo image",
                        null=True,
                        upload_to="school_logos/",
                    ),
                ),
                (
                    "geolocation",
                    django.contrib.gis.db.models.fields.PointField(srid=4326),
                ),
                (
                    "established_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="school.organization",
                    ),
                ),
            ],
        ),
    ]