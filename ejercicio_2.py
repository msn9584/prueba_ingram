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

def get_forcast_5_day_data(code_number):
    five_daily_adress = 'http://dataservice.accuweather.com/forecasts/v1/daily/5day/'+ code_number +'?apikey='+ api +'&details'
    with urllib.request.urlopen(five_daily_adress) as five_daily_adress:
        data = json.loads(five_daily_adress.read().decode())
    return(data)
    
def five_days_forecast(city, code, number_days = 1):
    code_number = get_city_code_number(city, code)
    data =  get_forcast_5_day_data(code_number)
    for fecha in data['DailyForecasts'][0:number_days]:
        print(datetime.strptime(fecha['Date'][0:10], '%Y-%m-%d').strftime('%d %b, %Y').upper())
        print('Weather: ' + fecha['Day']['IconPhrase'])
        print('Temperature: ' + str(round(((fecha['Temperature']['Maximum']['Value'] + fecha['Temperature']['Minimum']['Value'])/2 - 32) / 1.8, 1)) + ' Cº')
        
city,code = input('City,City code,n_days: ').split(',')

number_day = input('Number of days for the forecast (default = 1): ')
if not number_day.isdigit():
    number_day = 1
else:
    number_day = number_day

if not re.match("^[A-Za-z]+$", city) and re.match("^[A-Za-z]{2,3}$", code) and re.match("[0-5]+", number_day):
    print('Possibly you have entered the data wrong, put the name of the country followed by a comma, the country code without spaces followed by a comma and the number of days (max 5 days)')
else:
    five_days_forecast(city, code, int(number_day))
