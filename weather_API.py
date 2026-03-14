import requests
import json

api_key="a6d4400c1d0175ee68363b41940f4355"
city="Bhopal"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response=requests.get(url)

data=response.json()

print(data)   

print("city:",data["name"])
print("temperature:",data["main"]["temp"],"°C")
print("humidity:",data["main"]["humidity"],"%")

with open("weather_data.json","w")as file:
    json.dump(data,file,indent=4)