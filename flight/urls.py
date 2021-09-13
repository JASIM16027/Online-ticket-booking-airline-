from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'flight'
urlpatterns = [
    path('',views.index, name='index'),
    path("<int:flight_id>", views.flights, name='flights'),
    path("<int:flight_id>/book", views.book, name='book')

]

