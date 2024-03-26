import requests  #installed module using pip install requests. module for HTTP requests.
import tkinter as tk #GUI library
from tkinter import messagebox #imports messagebox module used for displaying dialogue boxes

def get_weather(api_key, location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return data

def display_weather():
    location = city_entry.get()
    api_key = '3e3ce3617c1b47e74dae06f009636d79'  # My API Key
    
    if not api_key:
        messagebox.showerror("API_key error", "Please Generate correct API Key!")
        return
    
    if not location:
        messagebox.showerror("Error", "Please enter a global location name!")
        return
    
    weather_data = get_weather(api_key, location)
    if weather_data['cod'] == 200:
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C", bg="#CCFFE5")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%",bg="#E5CCFF")
        wind_speed_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s",bg="#CCFFE5")
        weather_description_label.config(text=f"Weather Forecast: {weather_data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "location not found. Please try again.")

# Create the main window
root = tk.Tk()
root.geometry("400x300")
root.title("Monica's Weather App")
root.configure(bg="white")

# Create and place widgets
city_label = tk.Label(root, text="Which location's weather information would you like to see Today?")
city_label.pack(pady=20)

city_entry = tk.Entry(root)
city_entry.pack(pady=20)

get_weather_button = tk.Button(root, text="Show weather information", command=display_weather)
get_weather_button.pack()

temperature_label = tk.Label(root, text="")
temperature_label.pack()

humidity_label = tk.Label(root, text="")
humidity_label.pack()

wind_speed_label = tk.Label(root, text="")
wind_speed_label.pack()

weather_description_label = tk.Label(root, text="")
weather_description_label.pack()

# Run the application
root.mainloop()
