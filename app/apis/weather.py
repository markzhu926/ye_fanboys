import urllib.parse as urlparse, urllib.request as urlrequest
import json
from apis import getIpAddress

apiKey = "a591cc0b3ce141668cc142051211012"

ip = getIpAddress.getIp()

def getWeatherForCurrentLocation():
    try:
        url = "http://api.weatherapi.com/v1/current.json"
        params = {'key': apiKey, 'q': ip}

        urlParts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(urlParts[4]))
        query.update(params)
        
        urlParts[4] = urlparse.urlencode(query)
        siteData = urlrequest.urlopen(urlparse.urlunparse(urlParts))
        data = json.load(siteData)
        return data
    except Exception as issue:
        print('Unable to get weather location')
        print(issue)
        return {}

def getForecastForCurrentLocation():
    try:
        url = "http://api.weatherapi.com/v1/forecast.json"
        params = {'key': apiKey, 'q': ip}

        urlParts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(urlParts[4]))
        query.update(params)
        
        urlParts[4] = urlparse.urlencode(query)
        siteData = urlrequest.urlopen(urlparse.urlunparse(urlParts))
        data = json.load(siteData)
        return data
    except Exception as issue:
        print('Unable to get weather location')
        print(issue)
        return {}

# example formatting:

#{'location': {'name': 'Mount Vernon', 'region': 'Kansas', 'country': 'United States of America', 'lat': 37.72, 'lon': -97.85, 'tz_id': 'America/Chicago', 'localtime_epoch': 1640096702, 'localtime': '2021-12-21 8:25'}, 'current': {'last_updated_epoch': 1640096100, 'last_updated': '2021-12-21 08:15', 'temp_c': -5.3, 'temp_f': 22.5, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 0.0, 'wind_kph': 0.0, 'wind_degree': 0, 'wind_dir': 'N', 'pressure_mb': 1017.0, 'pressure_in': 30.03, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 81, 'cloud': 0, 'feelslike_c': -9.4, 'feelslike_f': 15.0, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 1.0, 'gust_mph': 12.3, 'gust_kph': 19.8}, 'forecast': {'forecastday': [{'date': '2021-12-21', 'date_epoch': 1640044800, 'day': {'maxtemp_c': 14.7, 'maxtemp_f': 58.5, 'mintemp_c': -3.1, 'mintemp_f': 26.4, 'avgtemp_c': 3.4, 'avgtemp_f': 38.1, 'maxwind_mph': 11.6, 'maxwind_kph': 18.7, 'totalprecip_mm': 0.0, 'totalprecip_in': 0.0, 'avgvis_km': 10.0, 'avgvis_miles': 6.0, 'avghumidity': 56.0, 'daily_will_it_rain': 0, 'daily_chance_of_rain': 0, 'daily_will_it_snow': 0, 'daily_chance_of_snow': 0, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'uv': 2.0}, 'astro': {'sunrise': '07:43 AM', 'sunset': '05:16 PM', 'moonrise': '07:28 PM', 'moonset': '09:53 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': '81'}, 'hour': [{'time_epoch': 1640066400, 'time': '2021-12-21 00:00', 'temp_c': -1.8, 'temp_f': 28.8, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 7.2, 'wind_kph': 11.5, 'wind_degree': 27, 'wind_dir': 'NNE', 'pressure_mb': 1025.0, 'pressure_in': 30.26, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 72, 'cloud': 0, 'feelslike_c': -5.9, 'feelslike_f': 21.4, 'windchill_c': -5.9, 'windchill_f': 21.4, 'heatindex_c': -1.8, 'heatindex_f': 28.8, 'dewpoint_c': -6.2, 'dewpoint_f': 20.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 15.0, 'gust_kph': 24.1, 'uv': 1.0}, {'time_epoch': 1640070000, 'time': '2021-12-21 01:00', 'temp_c': -2.3, 'temp_f': 27.9, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 6.0, 'wind_kph': 9.7, 'wind_degree': 29, 'wind_dir': 'NNE', 'pressure_mb': 1025.0, 'pressure_in': 30.25, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 73, 'cloud': 0, 'feelslike_c': -6.0, 'feelslike_f': 21.2, 'windchill_c': -6.0, 'windchill_f': 21.2, 'heatindex_c': -2.3, 'heatindex_f': 27.9, 'dewpoint_c': -6.5, 'dewpoint_f': 20.3, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.8, 'gust_kph': 20.5, 'uv': 1.0}, {'time_epoch': 1640073600, 'time': '2021-12-21 02:00', 'temp_c': -2.7, 'temp_f': 27.1, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 4.3, 'wind_kph': 6.8, 'wind_degree': 28, 'wind_dir': 'NNE', 'pressure_mb': 1024.0, 'pressure_in': 30.23, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 74, 'cloud': 0, 'feelslike_c': -5.5, 'feelslike_f': 22.1, 'windchill_c': -5.5, 'windchill_f': 22.1, 'heatindex_c': -2.7, 'heatindex_f': 27.1, 'dewpoint_c': -6.6, 'dewpoint_f': 20.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.9, 'gust_kph': 14.4, 'uv': 1.0}, {'time_epoch': 1640077200, 'time': '2021-12-21 03:00', 'temp_c': -3.0, 'temp_f': 26.6, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 2.5, 'wind_kph': 4.0, 'wind_degree': 19, 'wind_dir': 'NNE', 'pressure_mb': 1023.0, 'pressure_in': 30.21, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 76, 'cloud': 0, 'feelslike_c': -4.4, 'feelslike_f': 24.1, 'windchill_c': -4.4, 'windchill_f': 24.1, 'heatindex_c': -3.0, 'heatindex_f': 26.6, 'dewpoint_c': -6.6, 'dewpoint_f': 20.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 5.1, 'gust_kph': 8.3, 'uv': 1.0}, {'time_epoch': 1640080800, 'time': '2021-12-21 04:00', 'temp_c': -3.1, 'temp_f': 26.4, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 1.1, 'wind_kph': 1.8, 'wind_degree': 261, 'wind_dir': 'W', 'pressure_mb': 1022.0, 'pressure_in': 30.19, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 77, 'cloud': 0, 'feelslike_c': -3.1, 'feelslike_f': 26.4, 'windchill_c': -3.1, 'windchill_f': 26.4, 'heatindex_c': -3.1, 'heatindex_f': 26.4, 'dewpoint_c': -6.6, 'dewpoint_f': 20.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 2.5, 'gust_kph': 4.0, 'uv': 1.0}, {'time_epoch': 1640084400, 'time': '2021-12-21 05:00', 'temp_c': -3.0, 'temp_f': 26.6, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 2.9, 'wind_kph': 4.7, 'wind_degree': 238, 'wind_dir': 'WSW', 'pressure_mb': 1021.0, 'pressure_in': 30.16, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 76, 'cloud': 0, 'feelslike_c': -4.8, 'feelslike_f': 23.4, 'windchill_c': -4.8, 'windchill_f': 23.4, 'heatindex_c': -3.0, 'heatindex_f': 26.6, 'dewpoint_c': -6.7, 'dewpoint_f': 19.9, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 6.0, 'gust_kph': 9.7, 'uv': 1.0}, {'time_epoch': 1640088000, 'time': '2021-12-21 06:00', 'temp_c': -2.8, 'temp_f': 27.0, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 4.0, 'wind_kph': 6.5, 'wind_degree': 240, 'wind_dir': 'WSW', 'pressure_mb': 1021.0, 'pressure_in': 30.14, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 75, 'cloud': 0, 'feelslike_c': -5.5, 'feelslike_f': 22.1, 'windchill_c': -5.5, 'windchill_f': 22.1, 'heatindex_c': -2.8, 'heatindex_f': 27.0, 'dewpoint_c': -6.6, 'dewpoint_f': 20.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 8.5, 'gust_kph': 13.7, 'uv': 1.0}, {'time_epoch': 1640091600, 'time': '2021-12-21 07:00', 'temp_c': -2.7, 'temp_f': 27.1, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 247, 'wind_dir': 'WSW', 'pressure_mb': 1021.0, 'pressure_in': 30.14, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 74, 'cloud': 0, 'feelslike_c': -6.3, 'feelslike_f': 20.7, 'windchill_c': -6.3, 'windchill_f': 20.7, 'heatindex_c': -2.7, 'heatindex_f': 27.1, 'dewpoint_c': -6.6, 'dewpoint_f': 20.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.3, 'gust_kph': 19.8, 'uv': 1.0}, {'time_epoch': 1640095200, 'time': '2021-12-21 08:00', 'temp_c': -2.8, 'temp_f': 27.0, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 5.1, 'wind_kph': 8.3, 'wind_degree': 225, 'wind_dir': 'SW', 'pressure_mb': 1020.0, 'pressure_in': 30.13, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 75, 'cloud': 6, 'feelslike_c': -6.1, 'feelslike_f': 21.0, 'windchill_c': -6.1, 'windchill_f': 21.0, 'heatindex_c': -2.8, 'heatindex_f': 27.0, 'dewpoint_c': -6.5, 'dewpoint_f': 20.3, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 10.7, 'gust_kph': 17.3, 'uv': 2.0}, {'time_epoch': 1640098800, 'time': '2021-12-21 09:00', 'temp_c': -2.4, 'temp_f': 27.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 6.5, 'wind_kph': 10.4, 'wind_degree': 206, 'wind_dir': 'SSW', 'pressure_mb': 1020.0, 'pressure_in': 30.11, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 75, 'cloud': 33, 'feelslike_c': -6.3, 'feelslike_f': 20.7, 'windchill_c': -6.3, 'windchill_f': 20.7, 'heatindex_c': -2.4, 'heatindex_f': 27.7, 'dewpoint_c': -6.3, 'dewpoint_f': 20.7, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.6, 'gust_kph': 22.0, 'uv': 2.0}, {'time_epoch': 1640102400, 'time': '2021-12-21 10:00', 'temp_c': 0.4, 'temp_f': 32.7, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 8.1, 'wind_kph': 13.0, 'wind_degree': 212, 'wind_dir': 'SSW', 'pressure_mb': 1019.0, 'pressure_in': 30.09, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 62, 'cloud': 57, 'feelslike_c': -3.5, 'feelslike_f': 25.7, 'windchill_c': -3.5, 'windchill_f': 25.7, 'heatindex_c': 0.4, 'heatindex_f': 32.7, 'dewpoint_c': -5.9, 'dewpoint_f': 21.4, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 15.4, 'gust_kph': 24.8, 'uv': 2.0}, {'time_epoch': 1640106000, 'time': '2021-12-21 11:00', 'temp_c': 4.8, 'temp_f': 40.6, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 11.0, 'wind_kph': 17.6, 'wind_degree': 234, 'wind_dir': 'SW', 'pressure_mb': 1018.0, 'pressure_in': 30.07, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 51, 'cloud': 33, 'feelslike_c': 1.1, 'feelslike_f': 34.0, 'windchill_c': 1.1, 'windchill_f': 34.0, 'heatindex_c': 4.8, 'heatindex_f': 40.6, 'dewpoint_c': -4.4, 'dewpoint_f': 24.1, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.0, 'gust_kph': 20.9, 'uv': 2.0}, {'time_epoch': 1640109600, 'time': '2021-12-21 12:00', 'temp_c': 8.4, 'temp_f': 47.1, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 11.6, 'wind_kph': 18.7, 'wind_degree': 235, 'wind_dir': 'SW', 'pressure_mb': 1017.0, 'pressure_in': 30.03, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 44, 'cloud': 14, 'feelslike_c': 5.5, 'feelslike_f': 41.9, 'windchill_c': 5.5, 'windchill_f': 41.9, 'heatindex_c': 8.4, 'heatindex_f': 47.1, 'dewpoint_c': -3.2, 'dewpoint_f': 26.2, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.4, 'gust_kph': 21.6, 'uv': 3.0}, {'time_epoch': 1640113200, 'time': '2021-12-21 13:00', 'temp_c': 11.2, 'temp_f': 52.2, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 11.4, 'wind_kph': 18.4, 'wind_degree': 246, 'wind_dir': 'WSW', 'pressure_mb': 1015.0, 'pressure_in': 29.98, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 37, 'cloud': 18, 'feelslike_c': 9.0, 'feelslike_f': 48.2, 'windchill_c': 9.0, 'windchill_f': 48.2, 'heatindex_c': 11.2, 'heatindex_f': 52.2, 'dewpoint_c': -3.0, 'dewpoint_f': 26.6, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.2, 'gust_kph': 21.2, 'uv': 4.0}, {'time_epoch': 1640116800, 'time': '2021-12-21 14:00', 'temp_c': 13.4, 'temp_f': 56.1, 'is_day': 1, 'condition': {'text': 'Partly cloudy', 'icon': '//cdn.weatherapi.com/weather/64x64/day/116.png', 'code': 1003}, 'wind_mph': 10.3, 'wind_kph': 16.6, 'wind_degree': 288, 'wind_dir': 'WNW', 'pressure_mb': 1014.0, 'pressure_in': 29.95, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 29, 'cloud': 46, 'feelslike_c': 12.0, 'feelslike_f': 53.6, 'windchill_c': 12.0, 'windchill_f': 53.6, 'heatindex_c': 13.4, 'heatindex_f': 56.1, 'dewpoint_c': -4.2, 'dewpoint_f': 24.4, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 11.9, 'gust_kph': 19.1, 'uv': 4.0}, {'time_epoch': 1640120400, 'time': '2021-12-21 15:00', 'temp_c': 14.7, 'temp_f': 58.5, 'is_day': 1, 'condition': {'text': 'Overcast', 'icon': '//cdn.weatherapi.com/weather/64x64/day/122.png', 'code': 1009}, 'wind_mph': 8.5, 'wind_kph': 13.7, 'wind_degree': 319, 'wind_dir': 'NW', 'pressure_mb': 1013.0, 'pressure_in': 29.92, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 24, 'cloud': 95, 'feelslike_c': 13.8, 'feelslike_f': 56.8, 'windchill_c': 13.8, 'windchill_f': 56.8, 'heatindex_c': 14.7, 'heatindex_f': 58.5, 'dewpoint_c': -5.6, 'dewpoint_f': 21.9, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 9.8, 'gust_kph': 15.8, 'uv': 3.0}, {'time_epoch': 1640124000, 'time': '2021-12-21 16:00', 'temp_c': 14.3, 'temp_f': 57.7, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 11.4, 'wind_kph': 18.4, 'wind_degree': 8, 'wind_dir': 'N', 'pressure_mb': 1013.0, 'pressure_in': 29.92, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 25, 'cloud': 19, 'feelslike_c': 12.9, 'feelslike_f': 55.2, 'windchill_c': 12.9, 'windchill_f': 55.2, 'heatindex_c': 14.3, 'heatindex_f': 57.7, 'dewpoint_c': -5.3, 'dewpoint_f': 22.5, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 13.2, 'gust_kph': 21.2, 'uv': 4.0}, {'time_epoch': 1640127600, 'time': '2021-12-21 17:00', 'temp_c': 12.5, 'temp_f': 54.5, 'is_day': 1, 'condition': {'text': 'Sunny', 'icon': '//cdn.weatherapi.com/weather/64x64/day/113.png', 'code': 1000}, 'wind_mph': 11.0, 'wind_kph': 17.6, 'wind_degree': 20, 'wind_dir': 'NNE', 'pressure_mb': 1014.0, 'pressure_in': 29.95, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 32, 'cloud': 22, 'feelslike_c': 10.7, 'feelslike_f': 51.3, 'windchill_c': 10.7, 'windchill_f': 51.3, 'heatindex_c': 12.5, 'heatindex_f': 54.5, 'dewpoint_c': -3.5, 'dewpoint_f': 25.7, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 14.3, 'gust_kph': 23.0, 'uv': 4.0}, {'time_epoch': 1640131200, 'time': '2021-12-21 18:00', 'temp_c': 9.1, 'temp_f': 48.4, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 9.2, 'wind_kph': 14.8, 'wind_degree': 25, 'wind_dir': 'NNE', 'pressure_mb': 1016.0, 'pressure_in': 29.99, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 43, 'cloud': 4, 'feelslike_c': 6.8, 'feelslike_f': 44.2, 'windchill_c': 6.8, 'windchill_f': 44.2, 'heatindex_c': 9.1, 'heatindex_f': 48.4, 'dewpoint_c': -2.9, 'dewpoint_f': 26.8, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 16.3, 'gust_kph': 26.3, 'uv': 1.0}, {'time_epoch': 1640134800, 'time': '2021-12-21 19:00', 'temp_c': 6.4, 'temp_f': 43.5, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 9.4, 'wind_kph': 15.1, 'wind_degree': 41, 'wind_dir': 'NE', 'pressure_mb': 1017.0, 'pressure_in': 30.02, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 48, 'cloud': 6, 'feelslike_c': 3.5, 'feelslike_f': 38.3, 'windchill_c': 3.5, 'windchill_f': 38.3, 'heatindex_c': 6.4, 'heatindex_f': 43.5, 'dewpoint_c': -3.7, 'dewpoint_f': 25.3, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 19.7, 'gust_kph': 31.7, 'uv': 1.0}, {'time_epoch': 1640138400, 'time': '2021-12-21 20:00', 'temp_c': 4.1, 'temp_f': 39.4, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 8.5, 'wind_kph': 13.7, 'wind_degree': 52, 'wind_dir': 'NE', 'pressure_mb': 1017.0, 'pressure_in': 30.03, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 51, 'cloud': 5, 'feelslike_c': 0.9, 'feelslike_f': 33.6, 'windchill_c': 0.9, 'windchill_f': 33.6, 'heatindex_c': 4.1, 'heatindex_f': 39.4, 'dewpoint_c': -5.0, 'dewpoint_f': 23.0, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 17.9, 'gust_kph': 28.8, 'uv': 1.0}, {'time_epoch': 1640142000, 'time': '2021-12-21 21:00', 'temp_c': 3.4, 'temp_f': 38.1, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 6.9, 'wind_kph': 11.2, 'wind_degree': 52, 'wind_dir': 'NE', 'pressure_mb': 1018.0, 'pressure_in': 30.05, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 52, 'cloud': 2, 'feelslike_c': 0.5, 'feelslike_f': 32.9, 'windchill_c': 0.5, 'windchill_f': 32.9, 'heatindex_c': 3.4, 'heatindex_f': 38.1, 'dewpoint_c': -5.4, 'dewpoint_f': 22.3, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 14.5, 'gust_kph': 23.4, 'uv': 1.0}, {'time_epoch': 1640145600, 'time': '2021-12-21 22:00', 'temp_c': 2.9, 'temp_f': 37.2, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 5.8, 'wind_kph': 9.4, 'wind_degree': 57, 'wind_dir': 'ENE', 'pressure_mb': 1018.0, 'pressure_in': 30.06, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 53, 'cloud': 0, 'feelslike_c': 0.3, 'feelslike_f': 32.5, 'windchill_c': 0.3, 'windchill_f': 32.5, 'heatindex_c': 2.9, 'heatindex_f': 37.2, 'dewpoint_c': -5.8, 'dewpoint_f': 21.6, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.3, 'gust_kph': 19.8, 'uv': 1.0}, {'time_epoch': 1640149200, 'time': '2021-12-21 23:00', 'temp_c': 2.5, 'temp_f': 36.5, 'is_day': 0, 'condition': {'text': 'Clear', 'icon': '//cdn.weatherapi.com/weather/64x64/night/113.png', 'code': 1000}, 'wind_mph': 6.0, 'wind_kph': 9.7, 'wind_degree': 60, 'wind_dir': 'ENE', 'pressure_mb': 1018.0, 'pressure_in': 30.06, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 53, 'cloud': 0, 'feelslike_c': -0.3, 'feelslike_f': 31.5, 'windchill_c': -0.3, 'windchill_f': 31.5, 'heatindex_c': 2.5, 'heatindex_f': 36.5, 'dewpoint_c': -6.0, 'dewpoint_f': 21.2, 'will_it_rain': 0, 'chance_of_rain': 0, 'will_it_snow': 0, 'chance_of_snow': 0, 'vis_km': 10.0, 'vis_miles': 6.0, 'gust_mph': 12.8, 'gust_kph': 20.5, 'uv': 1.0}]}]}}

# example formatting:

# {'location': {'name': 'Washington Heights', 'region': 'New York', 'country': 'United States of America', 'lat': 40.85, 'lon': -73.94, 'tz_id': 'America/New_York', 'localtime_epoch': 1639617025, 'localtime': '2021-12-15 20:10'}, 'current': {'last_updated_epoch': 1639612800, 'last_updated': '2021-12-15 19:00', 'temp_c': 11.1, 'temp_f': 52.0, 'is_day': 0, 'condition': {'text': 'Overcast', 'icon': '//cdn.weatherapi.com/weather/64x64/night/122.png', 'code': 1009}, 'wind_mph': 0.0, 'wind_kph': 0.0, 'wind_degree': 164, 'wind_dir': 'SSE', 'pressure_mb': 1031.0, 'pressure_in': 30.43, 'precip_mm': 0.0, 'precip_in': 0.0, 'humidity': 71, 'cloud': 100, 'feelslike_c': 9.4, 'feelslike_f': 48.9, 'vis_km': 16.0, 'vis_miles': 9.0, 'uv': 1.0, 'gust_mph': 13.6, 'gust_kph': 22.0}}