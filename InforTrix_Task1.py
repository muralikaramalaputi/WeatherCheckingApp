import json
import requests

API_KEY = "3203f96f2a804ce3a2a145916240101"
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

def get_weather(city_name):
    params = {'q': city_name, 'key': API_KEY, 'aqi': 'no'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        weather_data = json.loads(response.text)
        return weather_data
    else:
        print('Returned Error Status Code.' ,response.status_code)
        return None

def main():
    while True:
        print('weather checking application')
        print('1.city name')
        print('2.exit')
        choice = input("enter the choice: ")
        if choice == '1':
            city_name = input('Enter the city name: ')
            weather_data = get_weather(city_name)
            if weather_data:
                temp_city = weather_data['current']['temp_c']
                humidity = weather_data['current']['humidity']
                wind_speed = weather_data['current']['wind_kph']
                local_time = weather_data['location']['localtime']
                print('----')
                print("weather stats for The City: '",format(city_name.upper()), "' ,at the Given Local Time: ", local_time)
                print('---')
                print('current temperature in Degree Celsius:', temp_city)
                print('current humidity      :', humidity, '%')
                print('current wind speed    :', wind_speed, 'Kph')
        elif choice == '2':
            print('exit')
            break
        else:
            print('invalid choice')
            break

main()
