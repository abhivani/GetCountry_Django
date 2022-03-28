from django.shortcuts import render
from .forms import PersonForm
# Create your views here.


# def index(request):
#     return render(request, 'Home.html')


def home(request):
    pf = PersonForm()
    return  render(request,'login.html',{'pf':pf})