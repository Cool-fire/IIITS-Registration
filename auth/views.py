# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .forms import SignupForm

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return HttpResponseRedirect('/home/')
    else:
        form = SignupForm()
    return render(request, 'auth/signup.html', {'form': form})