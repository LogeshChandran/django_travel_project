from django.shortcuts import render
from .forms import UsersForm
from .models import *

# Create your views here.
def home(request):
    services = Services.objects.all()
    locations = Location.objects.all()
    context = {'services': services,'locations':locations}
    return render(request, 'index.html', context)


def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

# def register(request):
#     return render(request,"register.html")

def locations(request):
    return render(request,"locations.html")

def locations_city(request,city):
    locations = Location.objects.get(cityName=city)
    context = {'location':locations}
    return render(request,"locations.html",context)

def register(request, *callback_args, **callback_kwargs):
    if request.method == 'POST':
        userModel = Users()
        mygender = request.POST.get('mygender')
        print(mygender)
        userModel.name = request.POST.get('myname')
        userModel.emailId = request.POST.get('myemail')
        userModel.phoneNumber = request.POST.get('myphone')
        userModel.age = request.POST.get('myage')
        userModel.gender = getGenderNumber(request.POST.get('mygender'))
        userModel.departuredate = request.POST.get('departuredate')
        userModel.departuretime = request.POST.get('departuretime')
        userModel.returndate = request.POST.get('returndate')
        userModel.returntime = request.POST.get('returntime')
        userModel.travelDestination = request.POST.get('td')
        userModel.package = request.POST.get('package')
        # if userModel.is_valid():
        print(userModel)
        userModel.save()
        return render(request, 'index.html')
    # else:
    #     form = UsersForm()
    #     context = {'form': form}
    return render(request, 'register.html')

def getGenderNumber(gender):
    if(gender == 'male'):
        return 0
    else:
        return 1
    
def setFlightServices():
    allFlightService = FlightService.objects.all()
    flightService = FlightService()
    flightService.image = '/static/images/l1.jpg'
    flightService.flight = "Flight " + str(len(allFlightService))
    flightService.save()

def setFoodServices():
    allFoodServices = FoodService.objects.all()
    foodService = FoodService()
    foodService.image = '/static/images/2a.jpg'
    foodService.food = "Food " + str(len(allFoodServices))
    foodService.save()

def setTravelService():
    allTravelService = TravelService.objects.all()
    travelService = TravelService()
    travelService.image = '/static/images/3a.jpg'
    travelService.travel = "Travel " + str(len(allTravelService))
    travelService.save()

def setHotelService():
    allHotelService = HotelService.objects.all()
    hotelService = HotelService()
    hotelService.image = '/static/images/4a.jpg'
    hotelService.hotel = "Hotel " + str(len(allHotelService))
    hotelService.save()

def setLocation(passlocation):
    location = Location()
    location.country = passlocation.country
    location.cityName = passlocation.cityName
    location.rating = passlocation.rating
    location.description = passlocation.description
    location.image = passlocation.image
    location.save()


def setService(passServices):
    allServices = Services.objects.all()
    services = Services()
    services.image = passServices.image
    services.serviceName = passServices.serviceName
    services.description = passServices.description
    services.save() 

# serices = ["Flight Services","Food Services","Travel Services","Hotel Services"]
# descriptions = ["Arrival and Departure","Catering","Pick-up/drop","Check-in/out"]
# images = ['/static/images/l1.jpg','/static/images/2a.jpg','/static/images/3a.jpg',
#           '/static/images/4a.jpg']
# for ind in range(len(serices)):
#     services = Services()
#     services.image = images[ind]
#     services.serviceName = serices[ind]
#     services.description = descriptions[ind]
#     setService(services) 





# countries = ["India","Turkey","France","Indonesia","United Arab Emirates","Switzerland","Andaman & Nicobar","Italy"]
# cityNames = ["Kashmir","Istanbul","Paris","Bali","Dubai","Geneva","Port Blair","Rome",]
# ratings = [5]
# descriptions = ["Heaven on Earth Kashmir is one of the most beautiful travel destinations to visit in North India. Nowhere in India you will behold the scenic landscapes, icy glaciers, pristine lakes and lofty mountains as beautiful as Kashmir. Serenity and Tranquility redefines itself from the ambiance of Kashmir. Be it summer, Winter or Monsoon, every season has its own charm in Kashmir. The numerous wonders of nature, culture, cuisines and rich history of Kashmir will elevate your travel experience in Incredible India."]
# images = ["/static/images/l1.jpg"]
# for ind in range(len(countries)):
#     location = Location()
#     location.country = countries[ind]
#     location.cityName = cityNames[ind]
#     location.rating = 5
#     location.description = descriptions[0]
#     location.image = "/static/images/l{0}.jpg".format(ind+1)
#     setLocation(location)


# for i in range(5):
#     setFlightServices()
#     setFoodServices()
#     setTravelService()
#     setHotelService()

