from django.shortcuts import redirect, render
from .forms import PostForm, SignupForm
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request,'home.html',{'posts':posts})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def dashboard(request):
    posts = Post.objects.all()
    return render(request,'dashboard.html',{'posts':posts})

def addpage(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('dashboard')
    else:
        postform = PostForm()
        return render(request,'addpage.html',{'postform':postform})

def editpage(request,id):
    if request.method == "POST":
        pid = Post.objects.get(id=id)
        form = PostForm(request.POST,request.FILES,instance=pid)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        pid = Post.objects.get(id=id)
        form = PostForm(instance=pid)
        return render(request,'editpage.html',{'form':form}) 
def deletpost(request,id):
    pid = Post.objects.get(id=id)
    pid.delete()
    return redirect('dashboard')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,'you have successfully register !')
            return redirect('login')
        else:
            messages.error(request,'Invalid something')
            return redirect('signup')
    else:   
        sform = SignupForm()
        return render(request,'signup.html',{'form':sform})

def login(request):
    return render(request,'login.html')

def logout(request):
    # logout(request)
    return redirect('signup')