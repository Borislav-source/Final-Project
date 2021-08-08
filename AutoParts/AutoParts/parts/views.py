from django.shortcuts import render

from AutoParts.parts.models import Part, Product


def parts_groups_list(request, engine):
    context = {
        'parts': Part.objects.all(),
        'engine_id': engine,
    }

    return render(request, 'parts/parts-groups-list.html', context)


def parts_list(request, engine_id, part_id):
    context = {
        'enrollments': Product.objects.filter(engine_id=engine_id, part_id=part_id)
    }

    return render(request, 'parts/parts-list.html', context)


def part_details(request):
    pass
