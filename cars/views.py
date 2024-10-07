from django.shortcuts import render,get_object_or_404
from .models import Car, Manufacturer

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    other_cars = Car.objects.exclude(id=car_id)     
    return render(request, 'cars/car_detail.html', {'car': car, 'other_cars': other_cars})

