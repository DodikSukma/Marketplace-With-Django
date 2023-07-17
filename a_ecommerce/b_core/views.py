from django.shortcuts import render , redirect
from django.contrib.auth import login, logout, authenticate
# Create your views here.

# Membuat Fungsi Untuk index
def index(request):
    return render(request, 'b_core/index.html')

from django.contrib import messages
from .forms import SignupForm, LoginForm
# def loginPage(request):
#     form = LoginForm()
#     if request.method == 'POST':

#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)


#         if user is not None : 
#             login(request, user)
#             return redirect('index-page')
#         else :
#              # Eror Handling
#              messages.info(request, 'Username Atau Password Salah')

#     context = {'form':form}
#     return render(request, 'b_core/login.html', context)

# Membuat Fungsi Signup

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    context ={
        'form': form,
    }
    return render(request, 'b_core/signup.html', context)


