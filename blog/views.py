from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
@login_required(login_url='login')
def home_view(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'website/home.html', context)
