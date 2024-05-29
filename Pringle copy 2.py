import requests
from customtkinter import *
from PIL import Image


app = CTk()
app.title('Turtle')
app.geometry('1000x500')
app._set_appearance_mode("light")



title_label = CTkLabel(app, text = 'WeatherAPP™',font=('Arial', 25, 'bold'))
msg_label = CTkLabel(app, text="", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
temp_label = CTkLabel(app, text="", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
condition_label = CTkLabel(app, text="", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
wind_label = CTkLabel(app, text="", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
alert_label = CTkLabel(app, text="", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA')
msg_label2 = CTkLabel(app, text="Select city: ↓↓↓", text_color='Blue', font=('Arial', 25, 'bold'),fg_color= '#EBEBEA' )


filename1 = ""


name_entry = CTkEntry(app, font=('Arial', 25, 'bold'), corner_radius=32, bg_color = '#EBEBEA')

c_img = CTkImage(light_image=Image.open('/Users/bisheralmazloum/Public/Python /snowy.png'), size=(100, 100))
image_label = CTkLabel(app, image=c_img, text="")
image_label.pack()

ecity = ""




def update_weather(event):
 
 filename1 = '/Users/bisheralmazloum/Public/Python /snowy.png'
 ecity = ""
 ecity = name_entry.get()


 #Fetch weather information from OpenWeatherMap API
 api = '928c56960d62b32ac062752c50a07679'  

 cityid = '6094817'
 
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
        cityid = '6094817'  #Ottawa city ID

 apiurl = f'''http://api.openweathermap.org/data/2.5/weather?id={cityid}&appid={api}&units=metric'''
 response = requests.get(apiurl)

 
 if response.status_code == 200:
     data = response.json()
     cityname = data['name']
     temperature = data['main']['temp']
     condition = data['weather'][0]['description']
     windspeed = data['wind']['speed']
     alert = data.get('alerts')
     
    
    
     print(f"Weather for {cityname}")
     print("Temperature:", temperature)
     print("Wind speed", windspeed)
     print("Condition:", condition)
     print(data)
    
     msg_label.configure(text=f"Weather for {cityname}: ", font=('Arial', 20, 'bold'))
     temp_label.configure(text=f"Temperature: {temperature}°C", font=('Arial', 20, 'bold'))
     condition_label.configure(text=f"Condition: {condition}", font=('Arial', 20, 'bold'))
     wind_label.configure(text=f"Wind speed: {windspeed}m/s", font=('Arial', 20, 'bold'))
     alert_label.configure(text=f"Weather alerts: {alert}", font=('Arial', 20, 'bold'))
    
    
 else:
     print("Failed to fetch weather information.")

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

 
 image_label.configure(image=c_img)


name_entry.bind('<Return>', lambda event: update_weather(event))



update_weather(True)
title_label.pack()
msg_label.pack()
temp_label.pack()
condition_label.pack()
wind_label.pack()
alert_label.pack()
msg_label2.pack()


name_entry.pack()

app.mainloop()

