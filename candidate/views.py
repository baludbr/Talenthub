from django.shortcuts import render,get_object_or_404,HttpResponse
from admins.models import *
# Create your views here.
def openings(request):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        jobs=Job.objects.filter(application_status=True).values
        return render(request,"openings.html",{"jobs":jobs})
    return HttpResponse("Session Time out")
def job_detail(request,job_id):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        jobs=Job.objects.filter(application_status=True).values
        job = Job.objects.get(id=job_id, application_status=True)
        user=User.objects.get(email=request.session.get("email"))
        if(JobApplicants.objects.filter(job_id=job_id,candidate_id=user.id).values()):
            return render(request, "openings.html", {"msg": f"Already Applied","jobs":jobs})
        else:
            application = JobApplicants.objects.create(
                job_id=job_id,
                candidate_id=user.id,
                status="In Progress"
            )
            return render(request, "openings.html", {"msg": f"Applied for {job.title}","jobs":jobs})
    return HttpResponse("Session Time out")
def applied_jobs(request):
    if request.session['role']==Candidates_us.objects.get(user=User.objects.get(email=request.session['email'])).role:
        user = get_object_or_404(User, email=request.session.get("email"))
        job_ids = JobApplicants.objects.filter(candidate_id=user.id).values_list('job_id', flat=True)
        print(job_ids.values)
        jobs = Job.objects.filter(id__in=job_ids)
        applied_jobs = [
            {
                'job_title': job.title,
                'company': job.company,
                'salary': job.salary,
                'status': applicant.status
            }
            for job, applicant in zip(jobs, JobApplicants.objects.filter(candidate_id=user.id, job_id__in=job_ids))
        ]
        return render(request, "appliedjobs.html", {"jobs": applied_jobs})
    return HttpResponse("Session Time out")
# def applied_jobs(request):
#     user = get_object_or_404(User, email=request.session.get("email"))
#     job_ids = JobApplicants.objects.filter(candidate_id=user).values_list('job_id', flat=True)
#     jobs = Job.objects.filter(id__in=job_ids)
#     print(jobs)
#     applied_jobs = [
#         {
#             'job_title': job.title,
#             'company': job.company,
#             'salary': job.salary,
#             'status': JobApplicants.objects.get(candidate_id=user, job_id=job.id).status
#         }
#         for job in jobs
#     ]
#     print(applied_jobs)
#     return render(request, "appliedjobs.html", {"jobs": applied_jobs})


        