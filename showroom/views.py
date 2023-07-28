from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    brands = brand.objects.all()

    return render(request , 'showroom/home.html' , {'brands' : brands})

def models_page(request , brand_name):
    models_data = model.objects.filter(brand__name=brand_name)
    return render(request , 'showroom/models.html' , {'models' : models_data})    


def team_page(request):
    team_data = staff.objects.all()
    return render(request , 'showroom/team.html' , {'staffs':team_data})


def stock_page(request):
    models_data = model.objects.all()
    return render(request , 'showroom/stock.html' , {'models' : models_data})