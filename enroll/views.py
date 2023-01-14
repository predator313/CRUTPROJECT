from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showdata(request):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
    else:
        fm=StudentRegistration();
    return render(request,'enroll/addandshow.html',{'form':fm})
