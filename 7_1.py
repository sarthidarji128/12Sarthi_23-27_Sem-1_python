api_key="6126a5d84240bd19cddc584c3a690750"
import requests
import datetime
city=input("Enter city: ")
response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={api_key}&units=Metric")
a=response.json()
if 'message' in a:
    print("City not Found!")
else:
    print("\nCity:",city)
    print("Temperature:",a['main']['temp'],"C")
    print("Humidity:",a['main']['humidity'])
    print("Sunrise(IST):",datetime.datetime.fromtimestamp(a['sys']['sunrise']))
    print("Sunset(IST):",datetime.datetime.fromtimestamp(a['sys']['sunset']))