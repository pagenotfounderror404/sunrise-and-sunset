import datetime
from smtplib import *
import requests
lat=25.178577
long=88.246117

position={
    "lat":lat,
    "lng":long,
    "formatted":0,
}
sun_mov=requests.get(url="https://api.sunrise-sunset.org/json", params=position,verify=False)

# print(sun_mov.json())

sunrise=sun_mov.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset=sun_mov.json()["results"]["sunset"].split("T")[1].split(":")[0]

# sun_rise_and_sun_set=(sunrise,sunset)
# print(sun_rise_and_sun_set)
print(sunrise)
print(sunset)

now=datetime.datetime.now()

print(now.hour)

position=requests.get(url="http://api.open-notify.org/iss-now.json")
print(position.status_code)
position.raise_for_status()

data=position.json()["iss_position"]
sat_longitude=float(data["longitude"])
sat_latitude=float(data["latitude"])
exact_position=(sat_latitude,sat_latitude)
# print(exact_position)

if sat_longitude>=long-5 and sat_longitude<=long+5 and sat_latitude>=lat-5 and sat_latitude<=lat-5:
    if now.hour>=sunset or now.hour<=sunrise:
        my_email= "20193021.it@gmail.com"
        password="abcd1234()"
        with SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="ayush2000chakraborty@gmail.com",
                                msg=f"Subject:Look up \n\n The ISS satellite is over you.")
