# Generated by Django 4.2.5 on 2024-01-28 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admins", "0005_applicant_job_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobApplicants",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("job_id", models.BigIntegerField(null=True)),
                ("candidate_id", models.TextField(null=True)),
                ("status", models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.RemoveField(
            model_name="job",
            name="applicants",
        ),
    ]