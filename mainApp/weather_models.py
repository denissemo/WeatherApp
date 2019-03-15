import requests


class SimpleWeather:
    api_key = 'f84baa428cbb55cab32452c999b76fba'
    api_url = 'http://api.openweathermap.org/data/2.5/weather?&q={},UA&units=metric&APPID={}'

    def __init__(self, city):
        self._city = city
        self._cities = []
        r = requests.get(url=self.api_url.format(city, self.api_key))
        self.data = r.json()
        print(self.data)
        # self._zip_code = self.data['results'][0]

    @property
    def zip_code(self):
        return self._zip_code

    def __str__(self):
        return self._city
