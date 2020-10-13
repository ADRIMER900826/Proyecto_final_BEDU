import requests
import datetime



r = requests.get("https://api.covid19api.com/country/afghanistan")
datos_afghanistan= r.json()
confirmados_afghanistan= [ dato["Confirmed"] for dato in datos_afghanistan]
muertes_afghanistan= [ dato["Deaths"] for dato in datos_afghanistan]
fechas_afghanistan= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_afghanistan]

r = requests.get("https://api.covid19api.com/country/albania")
datos_albania= r.json()
confirmados_albania= [ dato["Confirmed"] for dato in datos_albania]
muertes_albania= [ dato["Deaths"] for dato in datos_albania]
fechas_albania= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_albania]

r = requests.get("https://api.covid19api.com/country/andorra")
datos_andorra= r.json()
confirmados_andorra= [ dato["Confirmed"] for dato in datos_andorra]
muertes_andorra= [ dato["Deaths"] for dato in datos_andorra]
fechas_andorra= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_andorra]

r = requests.get("https://api.covid19api.com/country/angola")
datos_angola= r.json()
confirmados_angola= [ dato["Confirmed"] for dato in datos_angola]
muertes_angola= [ dato["Deaths"] for dato in datos_angola]
fechas_angola= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_angola]
