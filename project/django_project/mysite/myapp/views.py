from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def gallery(request):
    return render(request, 'gallery.html')

def videos(request):
    return render(request, 'videos.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def service(request):
    return render(request, 'service.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def succeslogout(request):
    return render(request, 'succeslogout.html')