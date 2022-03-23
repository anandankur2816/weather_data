import requests
from api import *
import json
from twilio.rest import Client

my_lat = 57.5344101
my_long = 27.369563
client = Client(twilio_sid, twilio_auth_token)
parameters = {
    "appid": api_key,
    "lat": my_lat,
    "lon": my_long,
    "exclude": "current,daily,minutely"
}
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

data = response.json()
weather_data = data["hourly"]
cnt = 0
for curr in weather_data:
    if cnt >= 12:
        break
    curr_weather_id = curr["weather"][0]["id"]
    # print(curr_weather_id)
    if int(curr_weather_id) < 700:
        message = client.messages \
            .create(
            body="Bring an umbrella today",
            from_='+19402898714',
            to='+918102036794'
        )
        print(message.status)
        break
    cnt += 1
# print(data)
