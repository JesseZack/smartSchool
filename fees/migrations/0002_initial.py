# Generated by Django 4.2.5 on 2023-10-06 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("users", "0001_initial"),
        ("fees", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactionlog",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.staff",
            ),
        ),
        migrations.AddField(
            model_name="refund",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fees.invoice"
            ),
        ),
        migrations.AddField(
            model_name="refund",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.student"
            ),
        ),
        migrations.AddField(
            model_name="receipt",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fees.invoice"
            ),
        ),
        migrations.AddField(
            model_name="receipt",
            name="received_by",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.staff",
            ),
        ),
        migrations.AddField(
            model_name="receipt",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.student"
            ),
        ),
        migrations.AddField(
            model_name="payment",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fees.invoice"
            ),
        ),
        migrations.AddField(
            model_name="latefee",
            name="invoice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fees.invoice"
            ),
        ),
        migrations.AddField(
            model_name="latefee",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.student"
            ),
        ),
        migrations.AddField(
            model_name="invoice",
            name="fees",
            field=models.ManyToManyField(to="fees.feestructure"),
        ),
        migrations.AddField(
            model_name="invoice",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="users.student"
            ),
        ),
        migrations.AddField(
            model_name="feestructure",
            name="discount",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="fees.discount",
            ),
        ),
        migrations.AddField(
            model_name="expense",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="fees.expensecategory"
            ),
        ),
        migrations.AddField(
            model_name="balance",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="users.student"
            ),
        ),
    ]
