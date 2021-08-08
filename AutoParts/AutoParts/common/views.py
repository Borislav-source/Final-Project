from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from AutoParts.accounts.models import Profile
from AutoParts.common.models import SiteInformation


class IndexView(TemplateView):
    template_name = 'pages/index.html'


def garage(request):
    if request.user.is_authenticated:
        customer = Profile.objects.get(user=request.user)
        car = customer.car

        if car:
            return render(request, 'pages/garage.html', {'car': car})
        messages.success(request, 'You haven\'t add a car in Your profile.')
        return redirect('index')
    messages.success(request, "You need to be sign in!")
    return redirect('index')


def contacts(request):
    context = {
        'information': SiteInformation.objects.first()
    }
    return render(request, 'pages/contacts.html', context)
