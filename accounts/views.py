from django.shortcuts import render, redirect
from .forms import RegisterForm, SignInForm  #imported from forms.py and its function
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.http import is_safe_url

# Create your views here.
def signout_page(request):
    logout(request)
    return redirect("/")

def signin_page(request):
    signinform = SignInForm(request.POST or None)
    redirect_path = request.POST.get('next_url') or None
    #print(redirect_path)
    context = {'signinform':signinform,}

    if signinform.is_valid():
        user = authenticate(username=signinform.data.get('username'),password=signinform.data.get('pwd'))
        if user:
            login(request,user)
            if redirect_path is not None:
                if is_safe_url(redirect_path,request.get_host()):
                    return redirect(redirect_path)
            # return redirect("/")
            return redirect("home")
        else:
            context['errMsg']="Invalid Credentials!"
    return render(request,"accounts/login.html",context)

def register_page(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        #print(request.POST)
    else:
        form = RegisterForm()
    #OR form = RegisterForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        un = form.cleaned_data.get('username')
        fn = form.cleaned_data.get('firstname')
        ln = form.cleaned_data.get('lastname')
        email = form.cleaned_data.get('email')
        pwd = form.cleaned_data.get('pwd')
        user = User.objects.create_user(username=un,password=pwd,email=email,first_name=fn,last_name=ln)
        if user:
            context['msg'] = "User has been created successfully!"
            context['form'] = RegisterForm()
        else:
            context['msg'] = "Something Went Wrong please try again!"
        #print('OKAAY')
    return render(request,'accounts/register.html',{'form':form},context)