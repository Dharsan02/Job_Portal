from django.shortcuts import render,redirect
from .models import *
from authapp.models import *
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
@login_required
def home(request):
  sreach_query=request.GET.get("search")
  if sreach_query:
     all_data=JobPost.objects.filter(role__icontains=sreach_query)
  else:
    all_data=JobPost.objects.all()
  context={
    'data':all_data
  }
  return render(request,'home.html',context)
@login_required
def read(request,id):
  all_data=JobPost.objects.get(id=id)
  context={
    'data':all_data
  }
  return render(request,'view.html',context)
@login_required
def application(request,jobid):
  context={
    'data':Application.objects.all()
  }
  if request.method=="POST":
    job=JobPost.objects.get(id=jobid)
    user=request.user
    exp=request.POST.get('exp')
    location=request.POST.get('location')
    resume=request.FILES.get('resume')
    new_application=Application.objects.create(job=job,userdata=user,experience=exp,location=location,resume=resume)
    email=EmailMessage(
      subject=f"New Application for {job.role}",
      body=f"Candidate name {user.username} \nEmail {user.email} \nMobile_No {user.mobile_no} \n{exp} \n{location} \n{resume}",
      from_email=settings.EMAIL_HOST_USER,
      to=[job.reciver_email],
    )
    email.attach(resume.name,resume.read(),resume.content_type)
    email.send(fail_silently=True)

    return redirect('home')
  return render(request,'application.html',context)
def homepage(request):
  context={
    "data":""
  }
  return render(request,"homepage.html",context)

@login_required
def profileview(request):
    profile, created = Candidate_profile.objects.get_or_create(
        user=request.user,
        defaults={
            'location': '',
            'skills': '',
            'education':'',
            'experience': '',
            'projects': '',
            'summary': '',
            'resume':'',
        }
    )

    context = {"data": profile}
    return render(request, 'profile_view.html', context)


from django.shortcuts import render, redirect, get_object_or_404
@login_required
def profileupdated(request, userid):
    selected = get_object_or_404(Candidate_profile, user_id=userid)
    if request.user.id != userid:
        return redirect('profileview')

    if request.method == "POST":
        selected.user.username = request.POST.get('name')
        selected.user.email = request.POST.get('email')
        selected.user.mobile_no=request.POST.get('mobile_no')
        selected.location = request.POST.get('location')
        selected.skills = request.POST.get('skills')
        selected.education=request.POST.get('education')
        selected.experience = request.POST.get('experience')
        selected.projects = request.POST.get('projects')
        selected.summary = request.POST.get('summary')
        selected.resume = request.FILES.get('resume')

        selected.user.save()
        selected.save()

        return redirect('profileview')

    context = {"data": selected}
    return render(request, "profileupdate.html", context)

   


# Create your views here.
