import requests
from _datetime import datetime
from config import weather_token

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(f'Hello, {message.from_user.full_name}!\n'
                         f'Welcome to our Weather bot! \n'
                         f'Enter any city in the world to see the weather of the city!')


@router.message()
async def get_weather(message: Message):
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
            f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={weather_token}&units=metric"
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
        sunrise_timestamp = datetime.fromtimestamp(data['sys']['sunrise']).strftime("%Y-%m-%d %H:%M")
        sunset_timestamp = datetime.fromtimestamp(data['sys']['sunset']).strftime("%Y-%m-%d %H:%M")
        length_of_the_day = datetime.fromtimestamp(data['sys']['sunset']) - datetime.fromtimestamp(
            data['sys']['sunrise'])

        current_date = datetime.now()
        formatted_date = current_date.strftime("%d-%m-%Y")
        await message.answer(f'***** {formatted_date} *****\n\n'
                             f'Weather in city: {city}\n\n'
                             f'Temperature:     {cur_weather}°C {wd}\n\n'
                             f'Feels like:             {feels_like}°C\n\n'
                             f'Humidity:            {humidity}%\n\n'
                             f'Pressure:            {pressure} mmHg\n\n'
                             f'Wind speed:       {wind}km/h\n\n'
                             f'Sunrise:               {sunrise_timestamp}\n\n'
                             f'Sunset:                {sunset_timestamp}\n\n'
                             f'Length of the day:    {length_of_the_day}\n\n'
                             f'***** Good Luck! *****')
    except Exception as e:
        await message.reply(f'Error \U00002620 \n'
                            f'{message.text} not Found')
