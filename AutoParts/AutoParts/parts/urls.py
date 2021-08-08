from django.urls import path

from AutoParts.parts.views import parts_groups_list, parts_list

urlpatterns = [
    path('<int:engine>', parts_groups_list, name='parts groups list'),
    path('parts-list/<int:engine_id><int:part_id>', parts_list, name='parts list'),
]
