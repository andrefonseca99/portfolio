from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'personal_projects/pages/home.html')

def about(request):
    return render(request, 'personal_projects/pages/about.html')

def work(request):
    return render(request, 'personal_projects/pages/work.html')

def contact(request):
    return render(request, 'personal_projects/pages/contact.html')
