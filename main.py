import requests
from datetime import datetime
import smtplib
import mail
import time 

def Check():
    if abs(myLat - lat) < 5 and abs(myLng - lng) < 5:
        return True
    
myLat =  51.507351
myLng = -0.127758

parameters = {
    "lat": myLat,
    "lng": myLng,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()["results"]
sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["sunset"].split("T")[1].split(":")[0])
hour = datetime.now().hour

issResponse = requests.get("http://api.open-notify.org/iss-now.json#")
issResponse.raise_for_status()
data = issResponse.json()["iss_position"]
lat = float(data["latitude"])
lng = float(data["longitude"])

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=mail.email,password=mail.code)

print(lat)
print(lng)

# while True:
#     time.sleep(60)
#     if Check() and (sunrise >= hour >= sunset): #testing dark later
#         subject = "Look up! The ISS is nearby"
#         body = "The ISS is currently overhead and it's dark outside. Go check it out!"
#         message = f"Subject: {subject}\n\n{body}"
#         connection.sendmail(from_addr=mail.email, to_addrs=mail.email, msg=message)
#         connection.quit()