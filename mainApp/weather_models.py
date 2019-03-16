import requests


images = {
    "01d": "https://images.unsplash.com/photo-1471341467792-4316ae7d02f7?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "02n": "https://images.unsplash.com/photo-1506599508865-f9ccc06cb8d9?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "02d": "https://images.unsplash.com/photo-1450005601738-ad61825d7281?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "03d": "https://newswalser.files.wordpress.com/2017/05/cropped-img_3925-gross.jpg",
    "03n": "https://images.unsplash.com/photo-1464014161740-a4ee1bf0fda6?ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&a"
           "mp;w=1000&amp;q=80",
    "04d": "https://c.pxhere.com/photos/c7/82/sky_storm_green_grass_animals_clouds_cloudy_overcast-500640.jpg!d",
    "04n": "https://images.unsplash.com/photo-1444086628530-dcb6e99a2481?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "09d": "https://subwallpaper.com/Widescreen-Wallpapers/spring-rain-background-For-Widescreen-Wallpaper.jpg",
    "09n": "https://subwallpaper.com/Widescreen-Wallpapers/spring-rain-background-For-Widescreen-Wallpaper.jpg",
    "10d": "https://subwallpaper.com/Widescreen-Wallpapers/spring-rain-background-For-Widescreen-Wallpaper.jpg",
    "10n": "https://subwallpaper.com/Widescreen-Wallpapers/spring-rain-background-For-Widescreen-Wallpaper.jpg",
    "11d": "https://images.unsplash.com/photo-1475116127127-e3ce09ee84e1?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "11n": "https://images.unsplash.com/photo-1475116127127-e3ce09ee84e1?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "13d": "https://images.unsplash.com/photo-1491002052546-bf38f186af56?ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&a"
           "mp;w=1000&amp;q=80",
    "13n": "https://images.unsplash.com/photo-1491002052546-bf38f186af56?ixlib=rb-1.2.1&amp;auto=format&amp;fit=crop&a"
           "mp;w=1000&amp;q=80",
    "50d": "https://images.unsplash.com/photo-1478601944016-d4fe7cba47c9?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80",
    "50n": "https://images.unsplash.com/photo-1478601944016-d4fe7cba47c9?ixlib=rb-1.2.1&amp;ixid=eyJhcHBfaWQiOjEyMDd9&a"
           "mp;auto=format&amp;fit=crop&amp;w=1000&amp;q=80"
}


class SimpleWeather:
    api_key = 'f84baa428cbb55cab32452c999b76fba'
    api_url = 'http://api.openweathermap.org/data/2.5/weather?&q={}&units=metric&APPID={}'

    def __init__(self, city):
        self._city = city
        r = requests.get(url=self.api_url.format(city, self.api_key))
        self.data = r.json()
        self.isFound = False
        # print(self._data)
        if self.data['cod'] == 200:
            self.isFound = True
            self.temp = self.data['main']['temp']
            # print(self._temp)
            self.weather = self.data['weather'][0]['icon']
            self.weather_desc = self.data['weather'][0]['description']
            self.speed = self.data['wind']['speed']
            self.country = self.data['sys']['country']
            self.clouds = self.data['clouds']['all']
            self.bg = images[self.weather]

    @property
    def city(self):
        return self.data['name']

    def __str__(self):
        return self._city
