import requests
import sys

def get_weather(city_name):
    api_key = "1b94e0f9e21ba1705bdb099dc0f8e2d2"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()
        #Print the temperature and weather condition
        if response.status_code == 200:
            print(f"Weather in {city_name}:")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")
        else:
            print(F"Error fetching weather data for '{city_name} ")
    except requests.exceptions.RequestException as e:
        print("An error occurred while fetching the weather data:", e)
 

    #call the function
city = sys.argv[1] if len(sys.argv) > 1 else "Bengaluru"
get_weather(city)