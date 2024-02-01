# Generated by Django 4.1.13 on 2024-01-25 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admins", "0002_remove_applicant_name_remove_applicant_resume"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="application_deadline",
        ),
        migrations.AddField(
            model_name="job",
            name="application_status",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="job",
            name="applicants",
            field=models.ManyToManyField(
                blank=True, related_name="jobs_applied", to="admins.applicant"
            ),
        ),
    ]