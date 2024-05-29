import requests
from customtkinter import *
from PIL import Image

#because being modern is cool apparently

#Initialize Custom tkinter
app = CTk()
app.title('Turtle')
app.geometry('1000x500')
app._set_appearance_mode("light")


#Create labels to display info
title_label = CTkLabel(app, text = 'WeatherAPP™',font=('Arial', 25, 'bold'))
msg_label = CTkLabel(app, text="", text_color='Black', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
temp_label = CTkLabel(app, text="", text_color='Black', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
condition_label = CTkLabel(app, text="", text_color='Black', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
wind_label = CTkLabel(app, text="", text_color='Black', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
alert_label = CTkLabel(app, text="", text_color='Black', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
msg_label2 = CTkLabel(app, text="Select city: ↓↓↓", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA' )


filename1 = ""


name_entry = CTkEntry(app, font=('Arial', 25, 'bold'), corner_radius=32, bg_color = '#EBEBEA')

c_img = CTkImage(light_image=Image.open('/Users/bisheralmazloum/Public/Python /snowy.png'), size=(100, 100))
image_label = CTkLabel(app, image=c_img, text="")
image_label.pack()

ecity = ""



#main function
def update_weather(event):
 
 filename1 = '/Users/bisheralmazloum/Public/Python /snowy.png'
 ecity = ""
 ecity = name_entry.get()


 #Fetch weather information from OpenWeatherMap API
 #Of course, won't give away mine, you get the idea though.
 api = 'API_KEY'  

 cityid = '6094817'

 #City ID OpenWeather uses to identify cities. Evidently, more can be added.
 if ecity.lower() == "mecca" :
        cityid = '104515'
 elif ecity.lower() == "medina":
        cityid = '109223'
 elif ecity.lower() == "tokyo":
        cityid = '1850147'
 elif ecity.lower() == "dubai":
        cityid = '292224'
 elif ecity.lower() == "new york":
        cityid = '5128581'
 elif ecity.lower() == "paris":
        cityid = '6455259'
 elif ecity.lower() == 'london':
        cityid = '1006984'
 elif ecity.lower() == "shanghai":
        cityid = '1796236'
 elif ecity.lower() == 'djibouti':
       cityid = '223817'
 elif ecity.lower() == 'ottawa':
        cityid = '6094817'  

 #Requests API info from OpenWeather website with API Key
 apiurl = f'''http://api.openweathermap.org/data/2.5/weather?id={cityid}&appid={api}&units=metric'''
 response = requests.get(apiurl)

 #Gets data if API call is successful, meaning returned status code 200
 if response.status_code == 200:
     data = response.json()
     cityname = data['name']
     temperature = data['main']['temp']
     condition = data['weather'][0]['description']
     windspeed = data['wind']['speed']
     alert = data.get('alerts')
     
    
     #Displays data in console as raw information, for debugging, checking returned information, etc. 
     print(f"Weather for {cityname}")
     print("Temperature:", temperature)
     print("Wind speed", windspeed)
     print("Condition:", condition)
     print(data)

     #Configures labels 
     msg_label.configure(text=f"Weather for {cityname}: ", font=('Arial', 20, 'bold'))
     temp_label.configure(text=f"Temperature: {temperature}°C", font=('Arial', 20, 'bold'))
     condition_label.configure(text=f"Condition: {condition}", font=('Arial', 20, 'bold'))
     wind_label.configure(text=f"Wind speed: {windspeed}m/s", font=('Arial', 20, 'bold'))
     alert_label.configure(text=f"Weather alerts: {alert}", font=('Arial', 20, 'bold'))
    
    
 else:
     print("Failed to fetch weather information.")

 #Decides what image to show based on what type of weather in data() -> condition 
 #More can be added for less common weather (acid rain?)
 if 'rain' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /rainy.jpeg"))
 elif 'light rain' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /rainy.jpeg"))
 elif 'overcast clouds' in condition.lower():
         c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /cloudy.jpg"))
 elif 'broken clouds' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /cloudy.jpg"))
 elif 'sunny' in condition.lower():
         c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /sunny.png"))
 elif 'clear sky' in condition.lower():
         c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /sunny.png"))
 elif 'sun' in condition.lower():
        c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /sunny.png"))
 elif 'thunder storm' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /thunderstorm.png"))
 elif 'snowy' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /snowy.png"))
 elif 'snow' in condition.lower():
      c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /snowy.png"))
 elif 'haze' in condition.lower():
       c_img.configure(light_image=Image.open("/Users/bisheralmazloum/Public/Python /haze.png"))

 #Changes image when city is changed if the weather is different
 image_label.configure(image=c_img)

#Updates weather based on input name_entry
name_entry.bind('<Return>', lambda event: update_weather(event))


#Pack all labels and call function
update_weather(True)
title_label.pack()
msg_label.pack()
temp_label.pack()
condition_label.pack()
wind_label.pack()
alert_label.pack()
msg_label2.pack()
name_entry.pack()


#Tkinter mainloop to keep app running
app.mainloop()

