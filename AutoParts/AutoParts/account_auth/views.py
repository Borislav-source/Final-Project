from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from AutoParts.account_auth.forms import SignInForm, SignUpForm


def sign_in(request):
    if request.method == 'GET':
        context = {
            'form': SignInForm()
        }
        return render(request, 'pages/sign-in.html', context)
    form = SignInForm(request.POST)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('index')
    return render(request, 'pages/sign-in.html', {'form': form})


def sign_up(request):
    if request.method == 'GET':
        context = {
            'form': SignUpForm(),
        }
        return render(request, 'pages/sign-up.html', context)
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('sign in')
    return render(request, 'pages/sign-up.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('index')
