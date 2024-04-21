from django.http import HttpResponse
from relations.models import Car, Car_owner, Colors


def test(request):
    # car_owners = Car_owner.objects.all()
    # for car_owner in car_owners:
    #     print(car_owner.name)
    #     print(car_owner.owned_car.color.name)

    colors = Colors.objects.all()

    for color in colors:
        print(color.name)
        print(color.car.all())


    return HttpResponse('Listo')
