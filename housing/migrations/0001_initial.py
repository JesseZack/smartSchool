# Generated by Django 4.2.5 on 2023-10-06 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Hostel",
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
                ("address", models.TextField()),
                ("capacity", models.PositiveIntegerField()),
                ("logo", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="MaintenanceRequest",
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
                ("request_date", models.DateField()),
                ("description", models.TextField()),
                (
                    "status",
                    models.PositiveIntegerField(
                        choices=[(1, "Pending"), (2, "Completed")], default=1
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
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
                ("room_number", models.CharField(max_length=10)),
                ("capacity", models.PositiveIntegerField()),
                ("vacant_beds", models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="RoomAllocation",
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
                ("allocation_date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="StudentAccommodation",
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
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="housing.room"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Student Accommodation",
            },
        ),
    ]
