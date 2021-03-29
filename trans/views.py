from django.shortcuts import render
from trans.form import PersonForm
from trans.models import Person
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render(request,'trans/home.html')
    

def donnee_client(request):
    return render(request,'client/DASH.html')

def index(request):
    return render(request,'trans/index.html')

def donnee(request):
    return render(request,'client/donnee.html')
    
def login(request):
    return render(request,'trans/login.html')  

def client_deux(request):
    return render(request,'trans/client_deux.html') 
  
def choix_client(request):
    return render(request,'trans/choix_client.html')

def vocal_form(request):
    return render(request,'trans/vocal_form.html')

def enregistrement(request):
    return render(request,'trans/enregistrement.html')

def home1(request):
    return render(request,'trans/acceuil.html')

def register(request):

    if request.method == 'POST':
        form = UserCreationForm (request.POST)

        if form.is_valid() :
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password )
            return redirect('../../accounts/login',permanent=True)

    else :
        form = UserCreationForm()
    return render(request,'registration/register.html')

def liste_reservation(request):
     return redirect('http://localhost:5000/users',permanent=True)


def verify(request):
    return redirect('http://localhost:5000/auth/login',permanent=True)

def info_client(request):
    return render(request,'trans/info_client.html')

def boss_login(request):
    return render(request,'trans/boss_login.html')

def home2(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        form.save()
        return redirection(request)
    else :
        person = Person.objects.all()
        return render(request,'trans/client.html',{'person' : person})

def redirection(request):
    print('rediriger')
    return redirect('http://localhost:5000/auth/register', permanent=True)

def liste_client(request):
    person = Person.objects.all()
    return render(request,'trans/liste_client.html',{'client':person})