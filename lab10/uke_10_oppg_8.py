import json
import requests
from datetime import datetime, timedelta 
def weather_in_bergen_next_hour():
    # lagrer url for data
    url = "https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=60.386691&lon=5.294357"
    # header som identifiserer meg
    headers = {
        'User-Agent':'inf100.ii.uib.no amska9085'
    }
    # innholdet på siden før dekoding, en byte-string
    webpage = requests.get(url, headers=headers)
    # etter dekoding, en vanlig streng
    webpage_content = webpage.content.decode('utf-8')
    # konverterer JSON-streng til oppslagsverk
    d = json.loads(webpage_content)
    # henter dato og tid for akkurat nå
    now = datetime.today() 
    # modifiserer den til likt format som den i api-et
    now_modified = now.strftime("%Y-%m-%dT%H:00:00Z")
    # løper gjennom alle klokkeslettene
    for i in range(len(d["properties"]["timeseries"])):
        # sjekker om noen av klokkeslettene matcher med akkurat nå
        if d["properties"]["timeseries"][i]["time"] == now_modified:
            data = d["properties"]["timeseries"][i]["data"]["next_1_hours"]
            symbol = data["summary"]["symbol_code"]
            wind_speed = d["properties"]["timeseries"][i]["data"]["instant"]["details"]["wind_speed"]
            relative_humidity = d["properties"]["timeseries"][i]["data"]["instant"]["details"]["relative_humidity"]
            uv_index = d["properties"]["timeseries"][i]["data"]["instant"]["details"]["ultraviolet_index_clear_sky"]
            rain_prob = data["details"]["probability_of_precipitation"]
            temperature  = d["properties"]["timeseries"][i]["data"]["instant"]["details"]["air_temperature"]
            if rain_prob == 0:
                return f"Været i bergen neste time er {symbol} og {temperature} grader. Vindhastigheten er {wind_speed}m/s. Luft fuktigheten er {relative_humidity}% og UV-indeksen på {uv_index}"
            else: 
                rain_min = data["details"]["percipitation_amount_min"]
                rain_max = data["details"]["percipitation_amount_max"]
                return f"Været i Bergen neste time er {symbol} og {temperature} grader med {rain_prob} for regn. Minste mengde forventet er {rain_min} mens den største mengden er {rain_max}. Ellers er vindhastigheten på {wind_speed}m/s og luftfuktigheten på {relative_humidity}% og UV-indeksen på {uv_index}"
print(weather_in_bergen_next_hour())