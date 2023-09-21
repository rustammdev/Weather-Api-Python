from requests import request, get, post, RequestException
import pandas as pd

class Weather:
    def init(self, city = '', kun='', deg=0, mn_t = 0, mx_t = 0, sh_sp = 0) -> None:

        self.city = city
        self.kun = kun
        self.deegre = deg
        self.min_temp = mn_t
        self.max_temp = mx_t
        self.shamol_s = sh_sp

    def str(self) -> str:
        weather_dc = pd.DataFrame ({
            'Malumotlar' : ['Shaxar:', 'Kun:', 'Tempratura(c):', 'Eng yuqori tempratura:', 'Eng quyi tempratura:', 'Shamol tezligi(m/s):'],
            'Qiymatlar' : [location, self.kun, self.deegre, self.max_temp, self.min_temp, self.shamol_s]
        })
        return str(weather_dc)



if name == "main":

    print()
    print("Manzilingizni inglis tilida kiriting.")
    location = input('>>>>> ')
    try:
        #Weather Api key
        API_KEY = "1487f6fe5449e8775aa9d424d1da33b4"

        url = "https://api.openweathermap.org/data/2.5/weather"
        payload = {
            #city name
            'q' : location, 
            'appid' : API_KEY
        }

        res = get(url=url, params=payload)
        if res.status_code == 200:
            json_dc = res.json()

    except RequestException as re:
        print(f"Xatolik kodi {re}")

    wth = Weather()    
    wth.city = location
    wth.deegre = json_dc['main']['feels_like'] - 272.5
    wth.max_temp = json_dc['main']['temp_max'] - 272.5
    wth.min_temp = json_dc['main']['temp_min'] - 272.5
    wth.shamol_s = json_dc['wind']['speed']
    wth.kun = json_dc['weather'][0]['description']

    print(wth)
    print()
