from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post
from .forms import AddPostForm


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    if request.method == "POST":
        form = AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts,
        'add_post_form': form
    }
    return render(request, 'website/home.html', context)


@login_required(login_url='login')
def post_add_view(request):
    if request.method == "POST":
        form = AddPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {
        'form': form,
        'title': 'Add Post'
    }
    return render(request, "website/post_add.html", context)
