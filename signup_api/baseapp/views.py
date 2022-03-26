from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Courses, User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm
# Create your views here.
def home(request):
    context = {}
    return render(request,'baseapp/home.html',context)


def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('baseapp:home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('baseapp:welcome')
        else:
            messages.error(request,'Username or password does not exist')
    context = {'page':page}
    return render(request,'baseapp/register_login.html',context)

def LogoutPage(request):
    logout(request)
    return redirect('baseapp:home')

def register(request):
   
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        user = User.objects.create(username=username,email=email,password=password1)
        user.set_password(password1)
        user.save()
        return redirect('baseapp:welcome')

        # form = NewUserForm(request.POST)
        # if form.is_valid():
        #     user = form.save()
        #     login(request,user)
        #     return redirect('baseapp:welcome')
        # else:
        #     messages.error(request,'Unsuccessful registration, Invalid information')
        #     print(form.errors)
    # form = NewUserForm()            
    # return render(request,'baseapp/register_login.html',{'form':form})
    return render(request,'baseapp/register_login.html',{})

@login_required(login_url='baseapp:login')
def welcome(request):
    userId = request.user.id
    print(userId)
    courses = Courses.objects.filter(student = userId)
    
    context = {'courses':courses,'request':request}
    return render(request,'baseapp/welcome.html',context)