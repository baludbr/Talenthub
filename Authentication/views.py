from django.shortcuts import render,HttpResponse
from django.utils import timezone
from .models import *
import random
from django.core.mail import send_mail
from django.core.files.base import ContentFile
YEAR_CHOICES = [r for r in range(1975, timezone.now().year + 4)]
def mail(subject,message,tomail):
            email_from = "dwarampudibalajireddy@gmail.com"
            recipient_list =tomail
            send_mail(subject, message, email_from, [recipient_list],fail_silently=False)
def dashboard(request):
    return render(request,"index.html")
def register(request):
    global resume1
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        if(User.objects.filter(email=email).values()):
            return render(request, "register.html", {"yrs": YEAR_CHOICES,"msg":"Mail Found"})
        password=request.POST.get('password')
        con=int(request.POST.get('cont_no'))
        adh=int(request.POST.get('ad_no'))
        if(User.objects.filter(aadhar_no=adh).values()):
            return render(request, "register.html", {"yrs": YEAR_CHOICES,"msg":"Aadhar Not Found"})
        t_s=request.POST.get('t_s')
        t_p_y=int(request.POST.get('t_p_y'))
        t_m=request.POST.get('t_m')
        i_s=request.POST.get('i_s')
        i_p_y=int(request.POST.get('i_p_y'))
        i_m=request.POST.get('i_m')
        u_s=request.POST.get('u_s')
        u_p_y=request.POST.get('u_p_y')
        u_m=request.POST.get('u_m')
        o_s_s=request.POST.get('o_s_s')
        o_s=request.POST.get('o_s')
        o_p_y=request.POST.get('o_p_y')
        o_m=request.POST.get('o_m')
        user = {
                "name":name,
                "email":email,
                "password":password,
                "contact_no":int(con),
                "aadhar_no":int(adh)
            }
        quali ={
                "tenth_school":t_s,
                "tenth_passout_year":int(t_p_y),
                "tenth_marks":t_m,
                "inter_school":i_s,
                "inter_passout_year":int(i_p_y),
                "inter_marks":i_m,
                "ug_school":u_s,
                "ug_passout_year":int(u_p_y),
                "ug_marks":u_m,
                "oth_specialisation":(o_s_s if o_s_s else "NA"),
                "oth_school":(o_s if o_s else "NA"),
                "oth_passout_year":(int(o_p_y) if o_s!=1975 else 0),
                "oth_marks":(o_m if o_s else "NA"),
        }
        request.session['user']=user
        request.session['quali']=quali
        request.session['zoom']=request.POST['zoomid']
        resume_file = request.FILES.get("resume")
        resume_content = resume_file.read()
        resume1 = ContentFile(resume_content, name=resume_file.name)
        otp=random.randrange(100000, 1000000)
        request.session['otp']=otp
        print(otp)
        msg= f"Tq for registered into Talent Hub!!.Your OTP is {{otp}}"
        mail("OTP For Verification",msg,email)
        return render(request,"otp.html")
    return render(request, "register.html",{"yrs": YEAR_CHOICES})
def verification(request):
    try:
        otpp = int(request.POST['otp'])
        exp = int(request.session["otp"])
        print(otpp, exp)
        if otpp == exp:
            user_data = request.session.get("user")
            quali_data = request.session.get("quali")
            user = User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                contact_no=user_data['contact_no'],
                aadhar_no=user_data['aadhar_no']
            )
            qua = Qualifications.objects.create(
                tenth_school=quali_data['tenth_school'],
                tenth_passout_year=quali_data['tenth_passout_year'],
                tenth_marks=quali_data['tenth_marks'],
                inter_school=quali_data['inter_school'],
                inter_passout_year=quali_data['inter_passout_year'],
                inter_marks=quali_data['inter_marks'],
                ug_school=quali_data['ug_school'],
                ug_passout_year=quali_data['ug_passout_year'],
                ug_marks=quali_data['ug_marks'],
                oth_specialisation=quali_data['oth_specialisation'],
                oth_school=quali_data['oth_school'],
                oth_passout_year=quali_data['oth_passout_year'],
                oth_marks=quali_data['oth_marks']
            )
            cs = Candidates_us.objects.create(
                user=user,
                qualifications=qua,
                resume=resume1,
                zoom_id=request.session.get("zoom")
            )

            return render(request, "register.html", {"yrs": YEAR_CHOICES, "msg": "Success"})
        else:
            return render(request, "register.html", {"yrs": YEAR_CHOICES, "msg": "Wrong OTP"})
    except Exception as e:
        print(str(e))
        return render(request, "register.html", {"yrs": YEAR_CHOICES, "msg": "Error occurred during verification"})
def login(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        x=User.objects.filter(email=email,password=password).values()
        if x:
                user=User.objects.get(email=email,password=password)
                cand=Candidates_us.objects.get(user=user)
                request.session['role']=cand.role
                request.session['email']=email
                return render(request,"nav.html",{"msg":cand.role})
        else:
            return render(request,"login.html",{"msg":"Invalid Credentaials"})
    return render(request,"login.html")  

def navbar(request):
    return render(request,'nav.html')
def profile(request):
    email=request.session.get("email")
    user=User.objects.get(email=email)
    cand_us=Candidates_us.objects.get(user=user)
    return render(request,"profile.html",{"candidate":cand_us})
def logout(request):
    request.session.flush()
    return render(request,'login.html',{"msg":"Logout Successfully"})        