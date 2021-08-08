from django.shortcuts import render

from AutoParts.vehicle.models import Vehicle, VehicleModels, Manufacturer


def vehicle_manufacturers(request, _type):
    context = {
        'manufacturers': Manufacturer.objects.all(),
        'type': _type,
    }

    return render(request, 'vehicles/vehicle-list-by-manufacturers.html', context)


def vehicle_models(request, pk, _type):
    context = {
        'vehicles': Vehicle.objects.filter(manufacturer_id=pk, vehicle_type=_type),
    }

    return render(request, 'vehicles/vehicle-list-by-models.html', context)


def vehicle_engines(request, model):
    vehicles = VehicleModels.objects.filter(pk=model)
    context = {
        'engine_list': [v.engine for v in vehicles],
    }
    return render(request, 'vehicles/vehicle-list-by-engine.html', context)
