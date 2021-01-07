import requests as req
from tkinter import *
import json
import time
import humanize 
from dotenv import load_dotenv
from os import getenv

load_dotenv()

top = Tk()
top.title("BitCoin tracker")
top.config(height=330, width=150)
top.geometry('330x150') 
top.wm_attributes("-topmost", 1)

key = getenv("NOMICS")

def getPrice():
    priceRes = json.loads(req.get("https://api.nomics.com/v1/currencies/ticker?key=" + key + "&ids=BTC").text)
    btc_usd = priceRes[0]["price"]
    text = "$"+humanize.intcomma(round(float(btc_usd), 3))
    if price.cget("text") != text:
        print(round(float(btc_usd), 3))
    return text

title = Label(top, text = "Real-time BTC tracker") 
unobtc = Label(top, text = "1₿ =") 
price = Label(top, text = "loading...") 

price.config(font=("Courier", 25))
unobtc.config(font=("Courier", 12))
title.config(font=("Courier", 18))

def update_label(label):
    label.configure(text=getPrice())
    top.after(5000, update_label, price)


title.place(relx=0.5, rely=0.2, anchor=CENTER)
unobtc.place(relx=0.5, rely=0.5, anchor=CENTER)
price.place(relx=0.5, rely=0.7, anchor=CENTER)
top.resizable(width=False, height=False)
top.after(500, update_label, price)
top.mainloop()  
