from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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


# class GarageView(LoginRequiredMixin, TemplateView):
#     template_name = 'pages/garage.html'
#     messages = 'You haven\'t add a car in Your profile.'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#
#         context['customer'] = Profile.objects.get(user=self.request.user)
#         return context


class ContactsView(TemplateView):
    template_name = 'pages/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['information'] = SiteInformation.objects.first()
        return context
