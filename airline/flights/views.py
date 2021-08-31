from django.shortcuts import render
from .models import Airport, Flight

# Create your views here.
def index(request):
    context = {}
    context['flights'] = Flight.objects.all()
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    context = {}
    context['flight'] = Flight.objects.get(id=flight_id)
    return render(request, 'flights/details.html', context)