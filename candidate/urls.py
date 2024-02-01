from django.urls import path,include
from .views import *
urlpatterns = [
    path("openings/",openings,name='openings'),
    path('job/<int:job_id>/', job_detail, name='application'),
    path("applied_jobs/",applied_jobs,name="applied"),
]