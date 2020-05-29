from django.shortcuts import render
import requests

def index(request):
    if request.method=="POST":
        api_address=" http://api.weatherapi.com/v1/forecast.json?key=<your_key>q="
        state=request.POST.get("select1")
        city=request.POST.get("select2")
        url=api_address+city+","+state+'&days=3'
        r=requests.get(url).json()
        city_weather={
            'city':city,
            'state':state,
            'country':'India',
            'temp_c':r['current']['temp_c'],
            'temp_f':r['current']['temp_f'],
            'date':r['location']['localtime'],
            'condition':r['current']['condition']['text'],
            'icon':r['current']['condition']['icon'],
            'day1':{
                'date1':r['forecast']['forecastday'][0]['date'],
                'max_temp':r['forecast']['forecastday'][0]['day']['maxtemp_c'],
                'min_temp': r['forecast']['forecastday'][0]['day']['mintemp_c'],
                'day1text':r['forecast']['forecastday'][0]['day']['condition']['text'],
                'day1icon': r['forecast']['forecastday'][0]['day']['condition']['icon'],
            },
            'day2':{
                'date2': r['forecast']['forecastday'][1]['date'],
                'max_temp': r['forecast']['forecastday'][1]['day']['maxtemp_c'],
                'min_temp': r['forecast']['forecastday'][1]['day']['mintemp_c'],
                'day2text': r['forecast']['forecastday'][1]['day']['condition']['text'],
                'day2icon': r['forecast']['forecastday'][1]['day']['condition']['icon'],
            },
            'day3':{
                'date3': r['forecast']['forecastday'][2]['date'],
                'max_temp': r['forecast']['forecastday'][2]['day']['maxtemp_c'],
                'min_temp': r['forecast']['forecastday'][2]['day']['mintemp_c'],
                'day3text': r['forecast']['forecastday'][2]['day']['condition']['text'],
                'day3icon': r['forecast']['forecastday'][2]['day']['condition']['icon'],
            }
        }
        #print(r)
        #print(city_weather.)
        context={'city_weather':city_weather}
        return render(request, 'index.html',context)
    return render(request, 'index.html')