from django.db import models
from Authentication.models import *
from .models import *
import datetime
class Job(models.Model):
    id=models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    published_at = models.DateTimeField(auto_now_add=True)
    application_deadline = models.DateField(blank=True,default=datetime.datetime.today)
    application_status = models.BooleanField(default=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

class JobApplicants(models.Model):
    id=models.AutoField(primary_key=True)
    job_id=models.BigIntegerField(null=True)
    candidate_id=models.TextField(null=True)
    status=models.CharField(max_length=1000,blank=True)