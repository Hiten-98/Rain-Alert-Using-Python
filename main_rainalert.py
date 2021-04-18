import requests
from twilio.rest import Client

#Your location
MY_LAT = 19.207237
MY_LONG = 72.834824

#API KEY of Twilio
account_sid = "Your Twilio API SID"
auth_token = "Your auth token"

#Parameters and API key for OpenWeatherMap
weather_parameters = {
    "lat": 17.361719,
    "lon": 78.475166,
    "appid": "459f0517e6d128acb671c38efff29e2d",
    "exclude": "current,minutely,daily",
}

#Getting data from OpenweatherApp
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()

#Filtering out the data in hourly basis
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

#Sending message
for hour_data in weather_slice:
    code = hour_data["weather"][0]["id"]
    if int(code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid,auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Bring Umbrella",
        from_='+18126128368', #This is Twilio's phone number
        to='Your phone number'
    )
    print(message.status)
