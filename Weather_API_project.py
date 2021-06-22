import requests #To make http or https requests
from datetime import datetime #To know the current time information

api_key = '5303707980149e325b9106eb31c85219' #API key of OPENWEATHERMAP
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link) #get the respone information
api_data = api_link.json() #Convert it into json format

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

file=open("Weather_info.txt","a") #open a file ,if not exist it create a new one

#writting content to the file
file.write("\n-------------------------------------------------------------\n")
file.write ("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
file.write ("-------------------------------------------------------------\n")

file.write ("Current temperature is: {:.2f} deg C\n".format(temp_city))
file.write ("Current weather desc  :{}\n".format(weather_desc))
file.write ("Current Humidity      :{} %\n".format(hmdt))
file.write ("Current wind speed    :{} kmph\n".format(wind_spd))

#close the file to avoid errors
file.close()

print("\nThe weather information of {} is successfully updated in the 'Weather_info.txt' file!\n".format(location.upper()))