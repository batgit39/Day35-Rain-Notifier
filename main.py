import json
import smtplib
import requests

MY_LOC = ""  
API_KEY = ""
END_POINT = "http://api.weatherapi.com/v1/forecast.json"
 
my_email = ""
password = ""

# fill your data

def send_mail():
    if is_gonna_rain():

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)
            connection.sendmail(
                    from_addr = my_email,
                    to_addrs = my_email,
                    msg = f"Subject:Bring Umbrella\n\nIts gonna rain today!"
                    )

def is_gonna_rain():
    parameters = {
        "q": MY_LOC, 
        "key": API_KEY,
        "days": 1
    }
     
    response = requests.get(url= END_POINT, params=parameters)
    response.raise_for_status()
    data = response.json()

    rain = False
    for i in range(7,23): # checking from 7:00 to 23:00
        code = data['forecast']['forecastday'][0]['hour'][i]['condition']['code']
        if code >= 1153: # you can change the code for any different conditions, the codes are provided in the weather conditions csv
            rain = True

    if rain:
        return True

send_mail()

#this is just for checking
# with open("weather_data.json", "w") as file:
    # json.dump(data, file)

