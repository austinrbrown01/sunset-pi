import subprocess
import json
import requests
import datetime
import time
from time import sleep

url = "http://api.openweathermap.org/data/2.5/weather"
query = {"q":"Phoenix","appid":"{MYAPPID}"}

while (True) :
    response = requests.request("GET",url,params=query)
    parsed = json.loads(response.text)
    sunrise = parsed["sys"]["sunrise"]
    sunset = parsed["sys"]["sunset"]
    millis = int(round(time.time()))
    print("Current time millis is %s" % millis)
    print("Sunset time is %s " % sunset)
    if (abs(millis - sunset) < (1500)):
        subprocess.call("./takePicture.sh", shell=True)
    sleep(300)


