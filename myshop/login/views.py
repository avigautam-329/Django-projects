from django.shortcuts import render,redirect
from django.http import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from .forms import *

def login(request):
    return render(request,'login.html')

def auth_view(request):
    
    username = request.POST['username']
    password = request.POST['password']
    m=User.objects.get(username=username)
    user = auth.authenticate(username=username,password=password)
    

    if user is not None:
        auth.login(request,user)
        #request.session['user_id']=m.id
        return redirect('orders:order_create',username)
    else:
        return HttpResponseRedirect('/invalid/')
        #return HttpResponse('Username Or password did not match..!')
        #form = RegistrationForm()
        #return render_to_response('login.html',{'form':form})
    """

    m=User.objects.get(username=username)
    if m.password == request.POST['password']:
        print "hello"
        request.session['user_id']=m.id
        return HttpResponse("You are logged in")
    else:
        return HttpResponse("Incorrect password")
    """   
def loggedin(request):
    if request.user.is_authenticated():
        return render(request,'loggedin.html',{'fullname':request.user.username})
    else:
        return HttpResponse('Page not found')

    
def invalid_login(request):
    return render(request,'invalid_login.html')

def logout(request):
    #print 'session:',request.session
    #del request.session['user_id']
    auth.logout(request)
    return HttpResponseRedirect('/')
        
    
def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            #form.save() or define save() in forms.py then call it...
            user = User.objects.create_user(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password1'],
            email = form.cleaned_data['email'])
            
            return redirect('mylogin:success')

    else:
        form = RegistrationForm()
    return render(request,'register.html',{'form':form})    


def register_success(request):
    
    return render(request,'register_success.html')
    


