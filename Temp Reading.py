# Simple code for running a DHT22 sensor. Utilizes the adafruit_dht repo and Tkinter. 
# Can display multiple measurements
# Kito Pang 2018 for Google Science Fair


from Tkinter import *
import time
import datetime
import Adafruit_DHT

window = Tk()
window.title("Temperature Reading")
window.geometry('480x320')
sensor = 22
pin = 4

def callback():
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    temp = int(temperature) * 9/5.0 +32
    time = datetime.datetime.now()
    lbl = Label(window, text=temp, font=("Arial Bold", 20))
    lbl.pack()
    lbl2 = Label(window, text = time.strftime("%r") + "     (In Farenheit above)", font=("Arial Bold", 15))
    lbl2.pack()
    
b = Button(window, text = "Refresh", command=callback)
b.pack()
          
window.mainloop()
