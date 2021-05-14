import pytz
import os
import time
from datetime import datetime

print("London, UK")
print("New York, America")
print("Berlin, Germany")
print("------------------")
country_chosen = input("Please Enter a country shown on the list. Lowercase please!  :")

if country_chosen == ("london"):
  country_id = 'London'
  country_time_zone = pytz.timezone('Europe/London')
  country_time = datetime.now(country_time_zone)

elif country_chosen == ("new york"):
  country_id = 'New York'
  country_time_zone = pytz.timezone('America/New_York')
  country_time = datetime.now(country_time_zone)

elif country_chosen == ("berlin"):
  country_id = 'Berlin'
  country_time_zone = pytz.timezone('Europe/Berlin')
  country_time = datetime.now(country_time_zone)

else:
  print("Thats not correct please try again.")
  time.sleep(1.5)
  os.system("clear")
  print("Ending process in 3 seconds")
  time.sleep(1)
  os.system("clear")
  print("Ending process in 2 seconds")
  time.sleep(1)
  os.system("clear")
  print("Ending process in 1 seconds")
  time.sleep(1)
  os.system("clear")
  print("Ending process in 0 seconds")
  time.sleep(1)
  os.system("clear")
  print("Ending Process ..")
  time.sleep(0.3)
  os.system("clear")
  print("Ending Process. .")
  time.sleep(0.3)
  os.system("clear")
  print("Ending Process.. ")
  time.sleep(2)
  os.system("clear")
  exit()


time.sleep(0.5)
os.system("clear")
print(str(" In ") + country_id + country_time.strftime(" the Date is %d-%m-%y and the time is %H:%M"))
print("           ")
print("           ")
print("           ")
print("  _    _                      ")
print(" | |  | |                     ")
print(" | |__| |_   _ _ __  _ __ ____")
print(" |  __  | | | | '_ \| '__|_  /")
print(" | |  | | |_| | |_) | |   / / ")
print(" |_|  |_|\__, | .__/|_|  /___|")
print("          __/ | |             ")
print("         |___/|_|             ")
print("                 HYPRZ 2021 ©")
