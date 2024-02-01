from django.db import models
from django.utils import timezone

YEAR_CHOICES = [(r, r) for r in range(1975, timezone.now().year + 4)]

class User(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,blank=True)
    email = models.EmailField(null=True)
    password= models.CharField(max_length=100,null=True)
    contact_no = models.BigIntegerField(null=True)
    aadhar_no = models.BigIntegerField(null=True, unique=True)

    def __str__(self):
        return f"{self.name} {self.email}"
class Qualifications(models.Model):
    tenth_school = models.CharField(max_length=100, blank=True)
    tenth_passout_year = models.IntegerField('Year', choices=YEAR_CHOICES, default=timezone.now().year)
    tenth_marks = models.CharField(max_length=100, blank=True)
    
    inter_school = models.CharField(max_length=100, blank=True)
    inter_passout_year = models.IntegerField('Year', choices=YEAR_CHOICES, default=timezone.now().year)
    inter_marks = models.CharField(max_length=100, blank=True)
    
    ug_school = models.CharField(max_length=100, blank=True)
    ug_passout_year = models.IntegerField('Year', choices=YEAR_CHOICES, default=timezone.now().year)
    ug_marks = models.CharField(max_length=100, blank=True)
    
    oth_specialisation = models.CharField(max_length=100, blank=True)
    oth_school = models.CharField(max_length=100, blank=True)
    oth_passout_year = models.IntegerField('Year', choices=YEAR_CHOICES, default=timezone.now().year)
    oth_marks = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.ug_school} {self.ug_marks}"
class Candidates_us(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    qualifications = models.OneToOneField(Qualifications, on_delete=models.CASCADE, unique=True,blank=True)
    resume = models.FileField(upload_to='',blank=True)
    zoom_id = models.BigIntegerField(null=True)
    role= models.CharField(max_length=100,default="user")
    def __str__(self):
        return f"{self.user.id} {self.role}"
