from django.urls import path

from AutoParts.accounts.views import profile_details, change_profile_details

urlpatterns = [
    path('', profile_details, name='profile details'),
    path('account-change/', change_profile_details, name='change profile'),
]

