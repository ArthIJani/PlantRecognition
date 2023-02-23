from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm,SignUpForm,BlogPostForm
from .models import Image,BlogPost



#--------------------                           Main Page                      -----------------------------------
def index(request):
    image = None
    if request.method == 'POST':
        image_file = request.FILES.get('image_file')
        if image_file:
            # Save the uploaded image file to the database
            image = Image(image_file=image_file)
            image.save()

            return render(request,'index.html')
    return render(request, 'index.html', {'image': image})



def about(request):
    return render(request, 'about.html')

#--------------------                           Blogs View                      -----------------------------------

#Create Blog
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect('blog_list')
    else:
        form = BlogPostForm()
    return render(request, 'explore.html', {'form': form})

#Blog Listing
def blog_list(request):
    posts = BlogPost.objects.all().order_by('-date_created')
    return render(request, 'blog_list.html', {'posts': posts})

#Blog Details
def blog_detail(request, pk):
    post = BlogPost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'post': post})

#--------------------                           SignUP                     -----------------------------------

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

#--------------------                           Login Page                    -----------------------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})





