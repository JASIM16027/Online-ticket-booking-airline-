from django.contrib import admin
from .models import Flight, Airport,Passenger


# Register your models here.
@admin.register(Flight)
class FlightModelAdmin(admin.ModelAdmin):
    list_display = ['id','origin','destination','duration']

@admin.register(Airport)
class AirportModelAdmin(admin.ModelAdmin):
    list_display = ['id','code','city']

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal=('flights',)
admin.site.register(Passenger, PassengerAdmin)

