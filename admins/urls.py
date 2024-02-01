from .views import *
from Authentication.views import *
from django.urls import path,include

urlpatterns = [
    path("",addjob,name='add_job'),
    path("list/",create_job,name="lists"),
    path('applicants/<int:job_id>/',showparticipants, name='applicants_job'),
    path('update/<int:user_id>/<int:job_id>/',statusupdate,name='update_status'),
    path('interviews/',interviews,name='interview')
]