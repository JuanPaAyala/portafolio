from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, "pages/index.html", {})

def projects(request):
    return render(request, "pages/projects.html", {})

@login_required
def resume(request):
    return render(request, "pages/resume.html", {})

def contact(request):
    return render(request, "pages/contact.html", {})
