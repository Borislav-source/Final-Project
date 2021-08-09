from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

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


class SignUpView(CreateView):
    template_name = 'pages/sign-up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)

        login(self.request, self.object)

        return result


def sign_out(request):
    logout(request)
    return redirect('index')
