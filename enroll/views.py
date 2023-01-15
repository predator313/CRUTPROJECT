from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
#def show data will used to insert and retrive the data from the database
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
    stud=User.objects.all() #to get all the stored data and indentation is also important otherwise 
    # the referenced before assigned error so take care of the proper indentation
    return render(request,'enroll/addandshow.html',{'form':fm,'stu':stud})


#delete_data() function is used to delete the data with the help of the dynamic urls
def delete_data(request,id):
    if(request.method=='POST'):
        del_x=User.objects.get(pk=id)
        del_x.delete()
        return HttpResponseRedirect('hello/student')
