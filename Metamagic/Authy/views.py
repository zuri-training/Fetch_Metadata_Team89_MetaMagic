from django.shortcuts import render, redirect
from .forms import LoginForm, NewUserForm, UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

# Create your views here.

def dashboard(request):
    return render(request, "Authy/dashboard.html")

def login(request):
    form = LoginForm(request.POST)
    if form.is_valid:
        pass
    else:
        form = LoginForm()

    context = {
        "form": form
    }
    return render(request, "Authy/registration/login.html", context)

# def register(request):
#     if request.method == "GET":
#         return render(
#             request, "registration/register.html",
#             {"form": UserCreationForm}
#         )
#     elif request.method == "POST":
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             messages.success(request, "Registration Successful.")
#             return redirect ("dashboard")
#         messages.error(request, "Unsuccessful registration. Invalid information. Please try again")
#     form = NewUserForm()
#     return render (request=request, template_name="registration/register.html", context={"register_form":form})

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = NewUserForm()

    context = {'form': form}
    return render(request, "registration/register.html", context)

    
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES["myFile"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, "Authy/upload.html", context)


# def index(request):
#     context = {}
#     if request.method == 'POST':
#         username = request.POST['username']
#         context = {'username': username}
#     return render(request, "index.html", context)

def home(request):
    return render(request, "Authy/index.html")

def contact(request):
    return render(request, "Authy/contact.html")

def about(request):
    return render(request, "Authy/about.html")

def metadisplay(request):
    return render(request, "Authy/Metadata-Display.html")

def metalibrary(request):
    return render(request, "Authy/metadata-library.html")

def profile(request):
    return render(request, "Authy/metadata-profile.html")

def metamodal(request):
    return render(request, "Authy/metadata.html")
