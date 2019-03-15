import requests


class SimpleWeather:
    api_key = 'NdGzFHswQ5vlPdzuWqGtG4vAhC6WmG1u '
    zip_code_url = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={}&q={}'

    def __init__(self, city):
        self._city = city
        self._zip_code = ""
        self._cities = []
        r = requests.get(url=self.zip_code_url.format(self.api_key, self._city))
        data = r.json()
        print(data)

    def __str__(self):
        return self._city
