import json
import time
import urllib.request
import re
from datetime import datetime


api = 'TaOaRYEv2bJ1wrWdCU8yJkGVuGC1tvr5'


def get_city_code_number(city, code):
    adress = 'https://dataservice.accuweather.com/locations/v1/cities/'+ code +'/search?apikey='+ api +'&q='+ city +'&details=true'
    with urllib.request.urlopen(adress) as adress:
        data = json.loads(adress.read().decode())
    code_number = data[0]['Key']
    return(code_number)

def get_current_day_data(code_number):
    daily_adress = 'http://dataservice.accuweather.com/currentconditions/v1/'+ code_number +'?apikey='+ api +'&details=false'
    with urllib.request.urlopen(daily_adress) as daily_adress:
        data = json.loads(daily_adress.read().decode())
    return(data)
    
def today_weather(city, code):
    code_number = get_city_code_number(city, code)
    data =  get_current_day_data(code_number)
    date = datetime.strptime(data[0]['LocalObservationDateTime'][0:10], '%Y-%m-%d')
    print(city.upper() + ' (' + code.upper() + ')')
    print(date.strftime('%d %b, %Y').upper())
    print('Weather: ' + data[0]['WeatherText'])
    print('Temperature: ' + str(data[0]['Temperature']['Metric']['Value']) + data[0]['Temperature']['Metric']['Unit'])    
    
city,code = input('City,City code: ').split(',')

if re.match("^[A-Za-z]+$", x) and re.match("^[A-Za-z]{2,3}$", y):
    print('Possibly you have entered the data wrong, put the name of the country followed by a comma and the country code without spaces')
else:
    today_weather(city, code)
