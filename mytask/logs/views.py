from email.policy import HTTP
from django.shortcuts import render

# Create your views here.
def manager(request):
    return render(request,'login_manager.html')
def admin(request):
    return render(request,'login_admin.html')
def index(request):
    return render(request,'index.html')