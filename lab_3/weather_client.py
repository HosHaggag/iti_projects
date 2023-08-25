import requests


class WeatherClient:

    def __init__(self, api_key="205774a49aea4bd299a135225232408"):
        self.api_key = api_key

    def get_current_temperature(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        return response.json()["current"]["temp_c"]

    def get_temperature_after(self, city, days, hour=None):
        url = f"http://api.weatherapi.com/v1/forecast.json?key={self.api_key}&q={city}&days={days}"
        response = requests.get(url)
        if hour:
            return response.json()["forecast"]["forecastday"][0]["hour"][hour]["temp_c"]
        return response.json()["forecast"]["forecastday"][0]["day"]["avgtemp_c"]

    def get_lat_and_long(self, city):
        url = f"http://api.weatherapi.com/v1/current.json?key={self.api_key}&q={city}"
        response = requests.get(url)
        return response.json()["location"]["lat"], response.json()["location"]["lon"]