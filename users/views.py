from django.shortcuts import render, redirect
from django.http import request
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UserRegisterForm
# Create your views here.  

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Accounted created for {username}!')
            return redirect(reverse_lazy('login'))
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})
@login_required
def profile(request):
    return render(request, 'profile.html')