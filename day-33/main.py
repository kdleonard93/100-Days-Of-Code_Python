import requests
from datetime import datetime
import smtplib
import time
from os import environ



MY_LAT = 41.878113 # Your latitude
MY_LONG = -87.629799 # Your longitude

PASSWORD = environ.get("EMAIL_PASSWORD")
SENDER_EMAIL = environ.get("SENDER_EMAIL")
SMTP_SERVER = environ.get("SMTP_SERVER")  
SMTP_PORT = int(environ.get("SMTP_PORT", 465)) 


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True
    
    
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    
    if time_now >= sunset or time_now <= sunrise:
        return True
    
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP(SMTP_SERVER)
        connection.starttls()
        connection.login(SENDER_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs="kdleonard@icloud.com",
            msg="Subject: Look up dawg 🔭 \n\nThe ISS is above you!"
        )
    else:
        print("Nothing up there yet 🌚")
    
    
