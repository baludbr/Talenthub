from django.shortcuts import render,HttpResponse
from Authentication.models import *
from .models import * 
# Create your views here.
def addjob(request):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            company = request.POST.get('company')
            location = request.POST.get('location')
            salary = request.POST.get('salary')
            email=request.session.get("email")
            print(email)
            user=User.objects.get(email=email)
            Job.objects.create(
                title=title,
                description=description,
                company=company,
                location=location,
                salary=salary,
                application_deadline=request.POST.get('deadline'),
                posted_by = user
            )
            return render(request,"addjob.html",{"msg":"Added Successfully"})
        return render(request,"addjob.html")
    return HttpResponse("Session Time out")


def create_job(request):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        email=request.session.get("email")
        user_id=User.objects.get(email=email)
        jobs=Job.objects.filter(posted_by=user_id)
        return render(request,"created_jobs.html",{"jobs":jobs})
    return HttpResponse("Session Time out")
def showparticipants(request, job_id):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        applicants = JobApplicants.objects.filter(job_id=job_id)
        users = User.objects.filter(id__in=[applicant.candidate_id for applicant in applicants])
        return render(request, 'show_participants.html', {'users': users,"jj":job_id})
    return HttpResponse("Session Time out")
def statusupdate(request,user_id,job_id):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        if request.method=='POST':
            print("Hello")
            return HttpResponse(J.status)
        print(user_id,job_id)
        J = JobApplicants.objects.get(job_id=job_id,candidate_id=user_id)
        request.session['update_user_id']=user_id
        request.session['update_job_id']=job_id
        user=User.objects.get(id=user_id)
        cand=Candidates_us.objects.get(user=user)
        print(J.status)
        print(cand.zoom_id)
        return render(request,"interview_schedule.html",{"status":J.status,"zoom_id":cand.zoom_id})
    return HttpResponse("Session Time out")
def interviews(request):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        if request.method=='POST':
            interview_date=request.POST['date']
            zoom_id=request.POST['zoomId']
            promotion=request.POST['promotion']
            user_id=request.session['update_user_id']
            user_mail=User.objects.get(id=user_id).email
            J = JobApplicants.objects.get(job_id=request.session['update_job_id'],candidate_id=request.session['update_user_id'])
            mail("Job Update",f"You are selected for {promotion}.We schedule a interview call with you on {interview_date} in Zoom {zoom}. All the Best",user_mail)
            print(f"You are selected for {promotion}.We schedule a interview call with you on {interview_date} in Zoom {zoom_id}. All the Best")
            J.status=promotion
            J.save()
            return render(request,"interview_schedule.html",{"status":J.status,"zoom_id":zoom_id})
    return HttpResponse("Session Time out")
    

