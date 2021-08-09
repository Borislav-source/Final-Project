from django.urls import reverse_lazy
from django.views.generic import FormView
from AutoParts.accounts.forms import ProfileForm
from AutoParts.accounts.models import Profile


class ProfileDetailsView(FormView):
    template_name = 'pages/profile-details.html'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['profile'] = Profile.objects.get(pk=self.request.user.id)

        return context


class ChangeProfileDetailsView(FormView):
    template_name = 'pages/change-profile-details.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile details')

    def form_valid(self, form):
        profile = Profile.objects.get(pk=self.request.user.id)
        profile.first_name = form.cleaned_data['first_name']
        profile.last_name = form.cleaned_data['last_name']
        profile.profile_picture = form.cleaned_data['profile_picture']
        profile.age = form.cleaned_data['age']
        profile.car = form.cleaned_data['car']
        profile.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        profile = Profile.objects.get(pk=self.request.user.id)
        context['form'] = ProfileForm(instance=profile)
        return context
