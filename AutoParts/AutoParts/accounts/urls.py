from django.urls import path

from AutoParts.accounts.views import ProfileDetailsView, ChangeProfileDetailsView

urlpatterns = [
    path('', ProfileDetailsView.as_view(), name='profile details'),
    path('account-change/', ChangeProfileDetailsView.as_view(), name='change profile'),
]

