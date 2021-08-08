from django.shortcuts import render, redirect
from AutoParts.accounts.forms import ProfileForm
from AutoParts.accounts.models import Profile
from AutoParts.vehicle.models import Vehicle


def profile_details(request):
    profile = Profile.objects.filter(pk=request.user)
    context = {
        'profile': profile[0],
    }
    return render(request, 'pages/profile-details.html', context)


def change_profile_details(request):
    profile = Profile.objects.get(pk=request.user.id)
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
        }
        return render(request, 'pages/change-profile-details.html', context)
    form = ProfileForm(request.POST, request.FILES, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile details')
    return render(request, 'pages/change-profile-details.html', {'form': form})

