import matplotlib.pyplot as plt
import requests
import json

def no2_concentration_in_bergen():
#  steg 1 last ned data fra meterologisk insittut
    url = "https://api.met.no/weatherapi/airqualityforecast/0.1/?lat=60.381288&lon=5.332430"
    headers = {
    # Noen nettsider krever at 'User-Agent' har fått en verdi
    # for at man skal få respons.
    'User-Agent': 'inf100.ii.uib.no amska9085', # Noe som forteller hvem du er
    }
    webpage = requests.get(url, headers=headers)
    dict_forecast = json.loads(webpage.content.decode('utf-8'))
    list_of_values = []
    list_of_times = []
    for entry in dict_forecast['data']['time']:
        list_of_times.append(entry['from'])
        list_of_values.append(entry['variables']['no2_concentration']['value'])
    for i in range(len(list_of_times)):
        print(list_of_times[i], list_of_values[i])
    plt.plot(list_of_times,list_of_values)
    plt.show()
no2_concentration_in_bergen()