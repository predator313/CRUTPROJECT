from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def showdata(request):
    if(request.method=='POST'):
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm=StudentRegistration() #this for clearing the form
            #we can also use the shortcut fm.save() directly instead of doing these
            #kinds of the cleaned data concept this is just a brilliant concept to deals with it
            #the below one is that if you want to save the particular data this below approch will best
            #if we want to save all data then we should use .save() function
            #  nm=fm.cleaned_data['name']
            #  em=fm.cleaned_data['email']
            #  pw=fm.cleaned_data['password']
            #  reg=User(name=nm,email=em,password=pw)
            #  reg.save()
    else:
        fm=StudentRegistration();
    return render(request,'enroll/addandshow.html',{'form':fm})
