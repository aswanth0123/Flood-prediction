from django.shortcuts import render,redirect
import requests
import math
from django.http import HttpResponse
from django.contrib import messages
from .graph import *
import datetime
import statistics


def monthly_rain(mon=None):
    data=pd.read_csv("flood/kerala.csv")
    month_list=data[mon]
    month_list.tolist()
    month_list=list(month_list)
    average = statistics.mean(month_list)
    return average


def month_change():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    months = [month.upper() for month in months]
    return months

def index(request):
        if request.method=='POST':
            city_name=request.POST['city']
            api_key='360e4bc3865e745ec844bd7ec054ca11'
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
            data=requests.get(url)
            weather_data = data.json()
            try:
                dt_object = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
                dt_object1 = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])
                request.method='GET'
            except:
                messages.success(request,'city not available')
                request.method='GET'
                return redirect(index)
        else:
            city_name='kochi'
            api_key='360e4bc3865e745ec844bd7ec054ca11'
            url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'
        try:
            data=requests.get(url)
            weather_data = data.json()
            dt_object = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
            dt_object1 = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])            
            x = datetime.datetime.now()
            x1=x.strftime("%b")
            monthly=monthly_rain(x1.upper())

            data={
                'city':city_name,
            # Extract relevant information
            'weather_description' : weather_data['weather'][0]['description'],
            'temperature_kelvin' : weather_data['main']['temp'],
            'temperature_celsius' : math.floor(weather_data['main']['temp'] - 273.15),  # Convert to Celsius
            'humidity' : weather_data['main']['humidity'],
            'temp_min_celsius' : math.floor(weather_data['main']['temp_min'] - 273.15),  # Convert to Celsius
            'temp_max_celsius' :math.floor(weather_data['main']['temp_max'] - 273.15),  # Convert to Celsius
            'sunrise': dt_object.strftime('%H:%M:%S'),'sunset': dt_object1.strftime('%H:%M:%S'),
            'monthly':round(monthly,2),
            'months':month_change()
            }
            return render(request,'index.html',{'data':data})
        except :
                messages.success(request,'please provide internet connection')
                return render(request,'index.html')

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
        a=predict1(year,l)
        if a[0]==1:
            messages.success(request,'There is a chance for Flood')
        else:
            messages.success(request,'There is no chance for Flood')
    return render(request,'predict.html')

def graph_view(request):
    year_list,rain_list=details_list()
    limit=[2900 for x in range(len(year_list))]
    return render(request,'graph.html',{'year_list':year_list,'rain_list':rain_list,'limit':limit})
   

def monthly_prediction(request):
    if request.method=='POST':
        month=request.POST['month']
        data=monthly_rain(month[:3])
        messages.success(request,'Predicted Rainfall of {} month is {}mm'.format(month,round(data,2)))
        return redirect(index)


