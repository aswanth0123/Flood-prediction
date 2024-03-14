from django.shortcuts import render
import requests
import math
from django.http import HttpResponse
from django.contrib import messages
from .graph import *
def index(request):
    try:
        city_name='kochi'
        api_key='360e4bc3865e745ec844bd7ec054ca11'
        url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        data=requests.get(url)
        weather_data = data.json()
        data={
            'city':city_name,
        # Extract relevant information
        'weather_description' : weather_data['weather'][0]['description'],
        'temperature_kelvin' : weather_data['main']['temp'],
        'temperature_celsius' : math.floor(weather_data['main']['temp'] - 273.15),  # Convert to Celsius
        'humidity' : weather_data['main']['humidity'],
        'temp_min_celsius' : math.floor(weather_data['main']['temp_min'] - 273.15),  # Convert to Celsius
        'temp_max_celsius' :math.floor(weather_data['main']['temp_max'] - 273.15),  # Convert to Celsius

        }
        return render(request,'index.html',{'data':data})

    except:
        return render(request,'index.html')
    # Display the weather details

from .prediction import *

def prediction(request):
    if request.method=='POST':
        year=float(request.POST['year'])
        January=float(request.POST['January'])
        February=float(request.POST['February'])
        March=float(request.POST['March'])
        April=float(request.POST['April'])
        May=float(request.POST['May'])
        June=float(request.POST['June'])
        July=float(request.POST['July'])
        August=float(request.POST['August'])
        September=float(request.POST['September'])
        October=float(request.POST['October'])
        November=float(request.POST['November'])
        December=float(request.POST['December'])
        l=[January,February,March,April,May,June,July,August,September,October,November,December]
        print(l)
        a=predict1(year,l)
        if a[0]==1:
            messages.success(request,'There is a chance for Flood')

        else:
            messages.success(request,'There is no chance for Flood')


    return render(request,'predict.html')


def graph_view(request):
    year_list,rain_list=details_list()
   
    return render(request,'graph.html',{'year_list':year_list,'rain_list':rain_list})
   