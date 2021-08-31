from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from .models import Airport, Flight, Passenger

# Create your views here.
def index(request):
    context = {}
    context['flights'] = Flight.objects.all()
    return render(request, 'flights/index.html', context)

def flight(request, flight_id):
    context = {}
    context['flight'] = Flight.objects.get(id=flight_id)
    context['passengers'] = context['flight'].passengers.all()
    return render(request, 'flights/details.html', context)

def book(request, flight_id):
    if request.method == 'POST':
        flight = Flight.objects.get(pk=flight_id)
        # TODO: check for duplicates
        passenger = Passenger.objects.create(first=request.POST['passenger_first'], last=request.POST['passenger_last'])
        passenger.save()
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse('details', args=(flight.id,)))