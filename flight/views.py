
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Flight,Passenger
from django.urls import reverse


# Create your views here.

def index(request):
    flights =Flight.objects.all()
    return render(request, 'flight/index.html',{'flights':flights})

def flights(request, flight_id):
    flights = Flight.objects.get(pk=flight_id)
    
    return render(request, 'flight/flights.html',{
        'flight':flights,
        'passengers':flights.passengers.all(),
        'non_passenger':Passenger.objects.exclude(flights=flights).all()
         

        })

def book(request, flight_id):
       
        if request.method=="POST":
            flight = Flight.objects.get(pk=flight_id)
    
            passenger =Passenger.objects.get(pk=int(request.POST['passengers']))
        
            passenger.flights.add(flight)

            return HttpResponseRedirect(reverse('flight:flights',args=(flight.id,)))
