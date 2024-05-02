from django.shortcuts import render, redirect




from django.http import HttpResponse 

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages 

from django.contrib.auth.models import User 

from django.contrib.auth.decorators import login_required










# Create your views her


def home(request):
    return render(request,"index.html")



def about(request):
    return render(request,"about.html")



def service(request):
    return render(request, "services.html")



def projects(request):
    return render(request,"projects.html")


def blogs(request):
    return render(request,"blogs.html")


def contact(request):
    return render(request,"contact.html")


def singnup(request):
    return render(request,"Singup.html")


def login(request):
    return render(request,"login.html")


def logout(request):
    return render(request,"logout.html")






# -------------------------------------------------------------
                  # Registration features  start
# -------------------------------------------------------------


# Create your views here.
def signup(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')                   
        try:
            if User.objects.get(username=email):
                # return HttpResponse("email already exist")
                messages.info(request,"Email is Taken")
                return render(request,'signup.html')
        except Exception as identifier:
            pass
        user = User.objects.create_user(email,email,password)
        user.is_active=False
        user.save()
        email_subject="Activate Your Account"
        message=render_to_string('activate.html',{
            'user':user,
            'domain':'127.0.0.1:8000',
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':generate_token.make_token(user)

        })

        # email_message = EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
        # email_message.send()
        messages.success(request,f"Activate Your Account by clicking the link in your gmail {message}")
        return redirect('/auth/login/')
    return render(request,"signup.html")

# -------------------------------------------------------------
                  # Registration features  end
# -------------------------------------------------------------

# -------------------------------------------------------------
                  # Login features  start
# -------------------------------------------------------------

def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return redirect('/')

        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/auth/login')

    return render(request,'login.html')  


# -------------------------------------------------------------
                  # Login features end
# -------------------------------------------------------------







