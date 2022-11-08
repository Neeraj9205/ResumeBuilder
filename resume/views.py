from urllib import response
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Resume2,Contact
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required 
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')   
def home(request):
    if request.method=='POST':
        vname=request.POST.get('name')
        vemail=request.POST.get('email')
        vphone=request.POST.get('phone')
        vdate_of_birth=request.POST.get('date_of_birth')
        vaddress=request.POST.get('address')
        vsummary=request.POST.get('summary')
        vhighschool=request.POST.get('highschool')
        vseniorschool=request.POST.get('seniorschool')
        vdegree=request.POST.get('degree')
        vuniversity=request.POST.get('university')
        vpreviouswork=request.POST.get('previouswork')
        vskills=request.POST.get('skills')
        vfathername=request.POST.get('fathername')
        vgender=request.POST.get('gender')
        vmaritalStatus=request.POST.get('MaritalStatus')
        vlanguage=request.POST.get('language')
        vnationality=request.POST.get('nationality')
        resume=Resume2(name=vname,email=vemail,phone=vphone,date_of_birth=vdate_of_birth,address=vaddress,summary=vsummary,highschool=vhighschool,
                seniorschool=vseniorschool,degree=vdegree,university=vuniversity,previous_work=vpreviouswork,
                skills=vskills,fathername=vfathername,gender=vgender,marital_status=vmaritalStatus,language=vlanguage,
                nationality=vnationality)    
        resume.save()
    return render(request,'home.html')

def Resumepdf(request,id):
    user_profile=Resume2.objects.get(id=id)
    template=loader.get_template('resumepdf.html')
    html=template.render({'user_profile':user_profile})
    options={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,options)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['content-Disposition']='attachment'
    filename='resume.pdf'
    return response
    #return render(request,'resumepdf.html',{'user_profile':user_profile})

def loadlogin(request):
    return render(request,'login.html') 
               
def loadregister(request):
    return render(request,'register.html') 


def register(request):
    if request.method == 'POST':
        vfname = request.POST.get('fname')
        vlname = request.POST.get('lname')
        vuname = request.POST.get('uname')
        vemail = request.POST.get('email')
        vpasswd = request.POST.get('passwd')
        vcpasswd = request.POST.get('cpasswd')
        if vpasswd == vcpasswd:
            if User.objects.filter(username=vuname).exists():
                messages.success(request, 'Username already exist')
                return redirect('/login')
            elif User.objects.filter(email=vemail).exists():
                messages.success(request, 'Email address is already registered..')
                return redirect('/')
            else:
                newuser = User.objects.create_user(first_name=vfname, last_name=vlname, username=vuname, email=vemail,password=vpasswd)
                newuser.save()
                messages.success(request, 'You have successfully registered')
                return render(request,'login.html')
                #return redirect('/userlogin')
        else:
            messages.success(request, 'Password is not matching....')
            return redirect('/')
    else:
        return render(request, 'register.html')


def Userlogin(request):
    if request.method=='POST':
        vuname=request.POST.get('uname')
        vpasswd=request.POST.get('passwd')
        newuser=auth.authenticate(username=vuname,password=vpasswd)
        if newuser is not None:
            auth.login(request,newuser)
            return redirect('/home')
        else:
            return render(request,'register.html')

@login_required(login_url='login')
def Userlogout(request):
    auth.logout(request)
    return render(request,'login.html')  


def listuser(request):
    user=Resume2.objects.all
    return render(request,'listuser.html', {'user':user})


def contact(request):
    if request.method=='POST':
        vname=request.POST.get('name')
        vemail=request.POST.get('email')
        vphone=request.POST.get('phone')
        vmessage=request.POST.get('message')
        details=Contact(name=vname,email=vemail,phone=vphone,message=vmessage)
        details.save()
    return render(request,'contact.html')    





