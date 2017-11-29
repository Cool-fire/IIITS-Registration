from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from upload.models import Document

@login_required()
def home(request):
    documents = Document.objects.all()
    return render(request,'website/home.html',{'documents': documents})

def ind(request):
    return render(request,'website/index.html')

def index(request):
    return render(request,'website/login.html')