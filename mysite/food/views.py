from django.shortcuts import render
from django.http import HttpResponse
from food.models import Item

# Create your views here.


def index(request):
    itemlist = Item.objects.all()
    return HttpResponse(itemlist)
def detail(request):
    return HttpResponse("<h1 style='color:green'>this is an details view</h1>")