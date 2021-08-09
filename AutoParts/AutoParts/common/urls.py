from django.urls import path, include
from AutoParts.common.views import IndexView, garage, ContactsView, GarageView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('accounts/', include('AutoParts.account_auth.urls')),
    path('vehicles/', include('AutoParts.vehicle.urls')),
    path('garage/', GarageView.as_view(), name='garage'),
    path('information/', ContactsView.as_view(), name='contacts'),
]