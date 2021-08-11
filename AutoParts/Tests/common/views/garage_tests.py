from django.urls import reverse
from django.utils.timezone import now

from AutoParts.accounts.models import Profile
from AutoParts.vehicle.models import EngineModel, Manufacturer, VehicleModels, Vehicle
from Tests.base.mixins import ProfileWithCarMixin
from Tests.base.tests import AutoPartsTestCase


class GarageViewTests(AutoPartsTestCase, ProfileWithCarMixin):


    def test_garage_view__if_right_template_is_used(self):
        profile = Profile.objects.get(pk=self.user)
        engine = EngineModel.objects.create(engine='1.8t')
        vehicle_manufacturer = Manufacturer.objects.create(name='Mercedes')
        vehicle_model = VehicleModels.objects.create(name='C-class', engine=engine, production_date=now())
        vehicle = Vehicle.objects.create(manufacturer=vehicle_manufacturer, vehicle_type='Car', model=vehicle_model)
        profile.car = vehicle
        profile.save()
        print(profile.car.model.engine.id)
        self.client.force_login(self.user)
        response = self.client.get(reverse('garage'), kwargs={'engine': vehicle.model.engine.id})
        self.assertTemplateUsed(response, 'pages/garage.html')

    def test__garage_view__without_logged_user(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('garage'))
        self.assertTemplateUsed(response, 'pages/garage.html')
