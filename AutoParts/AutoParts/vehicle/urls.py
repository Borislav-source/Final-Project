from django.urls import path

from AutoParts.vehicle.views import vehicle_models, vehicle_manufacturers, vehicle_engines

urlpatterns = [
    path('cars/<str:_type>', vehicle_manufacturers, name='cars'),
    path('car-models/<int:pk><str:_type>', vehicle_models, name='car models'),
    path('car-model-engines/<int:model>', vehicle_engines, name='vehicle engines'),
]
