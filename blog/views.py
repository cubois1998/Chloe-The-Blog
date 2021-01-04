from django.shortcuts import render, redirect


# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        context = {
            'title': 'Home'
        }
        return render(request, 'website/home.html', context)
    else:
        return redirect('login')
