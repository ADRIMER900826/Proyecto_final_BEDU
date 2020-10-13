import requests # Herramienta para obtener respuesta de  API
import datetime # Convertir formato fecha
import statistics # herramieta para obtener datos estadisticos 



#Se obtinen datos de la API
r = requests.get("https://api.covid19api.com/country/russian federation")
# formato JSON 
datos_russian_federation= r.json()
# Se seleccionan los casos confirmados 
confirmados_russian_federation= [ dato["Confirmed"] for dato in datos_russian_federation]
# Se seleccionan los casos de muertes 
muertes_russian_federation= [ dato["Deaths"] for dato in datos_russian_federation]
# Se convierten el formato fecha 
fechas_russian_federation= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_russian_federation]
# se obtinen los totales de la lista de confirmados 
total_confirmados_russian_federation= [sum (dato["Confirmed"] for dato in datos_russian_federation)]
# Se obtienen los totales de la lista de muertes
total_muertes_russian_federation = [ sum (dato["Deaths"] for dato in datos_russian_federation)]
# Se obtienen la desviacion estandar de la lista de confirmados "La desviación estándar es la medida de dispersión más común, que indica qué tan dispersos están los datos con respecto a la media. Mientras mayor sea la desviación estándar, mayor será la dispersión de los datos."
desvest_russian_federation_c= [statistics.stdev(confirmados_russian_federation)]
#Se obtiene la desviacion estandar de los casos de muertes
desvest_russian_federation_m = [statistics.stdev(muertes_russian_federation)]
#Se obtiene la mediana de la lista de confirmados "La mediana de un conjunto de números es el número medio en el conjunto".
mediana_russian_federation_c = [statistics.median(confirmados_russian_federation)]
#Se obtiene la mediana de la lista de muertes
mediana_russian_federation_m = [statistics.median(muertes_russian_federation)]
#Se obtiene el promedio de la lista de casos confirmados "es la suma de los datos dividida entre el número total de datos"
media_russian_federation_c= [statistics.mean(confirmados_russian_federation)]
#Se obtiene el promedio de la lista de casos de muerte
media_russian_federation_m = [statistics.mean(muertes_russian_federation)]





#Se repite lo mismo con cada país




r = requests.get("https://api.covid19api.com/country/angola")
datos_angola= r.json() 
confirmados_angola= [ dato["Confirmed"] for dato in datos_angola]
muertes_angola= [ dato["Deaths"] for dato in datos_angola]
fechas_angola= [ datetime.datetime.strptime(dato["Date"][0:10], "%Y-%m-%d") for dato in datos_angola]
total_confirmados_angola= [sum (dato["Confirmed"] for dato in datos_angola)]
total_muertes_angola = [ sum (dato["Deaths"] for dato in datos_angola)]

desvest_angola_c= [statistics.stdev(confirmados_angola)]
desvest_angola_m = [statistics.stdev(muertes_angola)]
mediana_angola_c = [statistics.median(confirmados_angola)]
mediana_angola_m = [statistics.median(muertes_angola)]
media_angola_c= [statistics.mean(confirmados_angola)]
media_angola_m = [statistics.mean(muertes_angola)]
