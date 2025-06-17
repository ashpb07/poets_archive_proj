from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from myproj import settings
from django.core.mail import send_mail,EmailMessage
from django.contrib.auth.decorators import login_required
from .forms import Memberform
from .models import Member

# Create your views here.


def home(request):
    return render(request,'home.html')
def signin(request):
    if request.method =='POST':
        
        username = request.POST['username']
        pass1 = request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
           # fname=user.first_name
           
        
            #next_url = request.GET.get('next')
            #return redirect(next_url if next_url else 'member')
            messages.success(request,'sucess')
            return redirect('member')  # ✅ Correct!

        else:
            messages.error(request,"invalid")
            return redirect('signin')
    return render(request,'signin.html')




    

def signout(request):
    logout(request)
    return redirect('home')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if User.objects.filter(username=username):
                messages.error(request,"username already exists")
                return redirect('signup')
        if User.objects.filter(email=email):
            messages.error(request,"email already exists")
            return redirect('signup')    

        if pass1 != pass2:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        # if User.objects.filter(username=username).exists():
        #     messages.error(request, "Username already exists.")
        #     return redirect('signup')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        # Member.objects.create(user=myuser)


        messages.success(request, "Signup successful!")



        subject="welcome to The Poet's Archive"
        message="hello,"+myuser.first_name
        from_email=settings.EMAIL_HOST_USER
        to_list=[myuser.email]
        email = EmailMessage(
            subject=subject,
                body='Hello,'+myuser.first_name,
        from_email=settings.EMAIL_HOST_USER,
            to=[myuser.email],
        )
        email.attach_file('C:\\vscode\\python\\pers_proj\\myproj\\email\\email_attach.png')

        
        email.send()

        #send_mail(subject,message,from_email,to_list,fail_silently=True )

        return redirect('signin')

    return render(request, 'signup.html')

        

def about(request):
    return render(request,'about.html')


def collection(request):
    return render(request,'collection.html')

def profile(request):
    return render(request,'profile.html')
    #     username = request.POST["username"]
    #     password = request.POST["password"]
    #     user = authenticate(request, username=username, password=password)
    #     if user is not None:
    #         login(request, user)
    #         # Redirect to a success page.
    #         return redirect('home')
    #     else:
    #         messages.success(request,("there was error "))
    #         return redirect('login.html')
    #         # Return an 'invalid login' error message.
    # else:
    #     return render(request,'signup.html')

@login_required
def member(request):
  
    
    return render(request,'member.html')

def publish(request):
    return render(request,'publish.html')

def learn(request):
    
    
        
    return render(request,'learn.html')