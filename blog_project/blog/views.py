from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog import models
from . models import Blog,Contact
from . form import ContactForm,PostBlogForm,UpdateBlogForm,CommentBlogForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.urls import reverse_lazy


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email= request.POST.get('uemail')
        password = request.POST.get('upassword')
        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()
        return redirect('/loginn')
    return render(request, 'signup.html')

def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            return redirect('/mypost')


        else:
            return redirect('/login')

    return render(request, 'login.html')

def myPost(request):
    all_blogs=Blog.objects.all()
    context={
        'blogs':all_blogs
    }
    return render(request, 'mypost.html',context)

def signout(request):
    logout(request)
    return redirect('/loginn')

def contactUs(request):
    form=ContactForm()
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request,"Your form is submitted successfully")
        else:
            form=ContactForm()
            
    return render(request,"contact_us.html",{'form':form})

def blog_detail(request,slug):
    blog = Blog.objects.get(slug=slug)
    all_blogs=Blog.objects.all().order_by('-post_date')[:10]
    form=CommentBlogForm()
    if request.method=="POST":
        form=CommentBlogForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your comment on this blog has been posted")
            return redirect("/blog_detail/"+blog.slug)
    else:
        form=CommentBlogForm()

    
    context={
        'blog':blog,
        'all_blogs':all_blogs,
        'form':form
    }
    return render(request,'blog_detail.html',context)

def profile(request,user_name):
    user_related_data=Blog.objects.filter(author__username=user_name)
    context={
        'user_related_data':user_related_data
    }
    return render(request,'profile.html',context)

class CreateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
    form_class = PostBlogForm
    template_name = "create_blog.html"
    login_url = 'login'
    success_url = "/mypost"
    success_message = "Your blog has been created"

class UpdateBlog(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model=Blog
    form_class = UpdateBlogForm

    template_name = "update_blog.html"
    login_url = 'login'
    success_url = "/mypost"
    success_message = "Your blog has been updated"

class DeleteBlog(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model=Blog
    template_name = "delete_blog.html"
    login_url = 'login'
    success_url = "/mypost"
    success_message = "Your blog has been deleted"

class DeleteUser(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = User
    login_url = 'login'
    template_name = 'delete_user.html'
    success_message = "User has been deleted"
    success_url = reverse_lazy('mypost')
    


