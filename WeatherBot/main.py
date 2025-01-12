import requests
from pprint import pprint
from config import weather_token
from datetime import datetime


def get_weather(city, open_weather_token):

    global wd
    code_to_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": 'Clouds \U00002681',
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002614",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Tuman \U0001F328"
    }

    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric"
        )
        data = r.json()

        city = data['name']

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            "Broken Clouds"

        cur_weather = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        feels_like = data['main']['feels_like']
        wind = data['wind']['speed']
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset'])
        length_of_the_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(
            data['sys']['sunrise'])

        current_date = datetime.now()
        formatted_date = current_date.strftime("%d-%m-%Y")
        print(f'*****{formatted_date}*****\n'
              f'Weather in city: {city}\n'
              f'Temperature: {cur_weather}°C {wd}\n'
              f'Feels like: {feels_like}°C\n'
              f'Humidity: {humidity}%\n'
              f'Pressure: {pressure} mmHg\n'
              f'Wind speed: {wind}\n'
              f'Sunrise: {sunrise_timestamp}\n'
              f'Sunset: {sunset_timestamp}\n'
              f'Length of the day: {length_of_the_day}\n'
              f'Good Luck!')
        # pprint(data)

    except Exception as e:
        print(f'{e} not Found')
        print("Error!")


def main():
    city = input("enter city name: ")
    get_weather(city, weather_token)


if __name__ == '__main__':
    main()
