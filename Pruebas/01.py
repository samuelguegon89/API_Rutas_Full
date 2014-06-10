#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json


origen=raw_input('Seleccione la ciudad origen: ')
destino=raw_input('Seleccione la ciudad destino: ')
listalatitud=['']
listalongitud=['']

url='http://maps.googleapis.com/maps/api/directions/json'
obtener=requests.get(url=url,params={'origin':origen,
									   'destination':destino,
									   'region':'ES',
									   'sensor':'false',
									   'avoid':'tolls',
									   'units':'metric',
									   'mode':'BUS'})


dicc = json.loads(obtener.text.encode("utf-8"))

contador=0
contadores=1
variable=''

for i in dicc['routes'][0]['legs'][0]['steps']:
	latitud= i['end_location']['lat']
	longitud= i['end_location']['lng']
	listalatitud.append(latitud)
	listalongitud.append(longitud)
	contador=contador+1
	
urlmapa='maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|weight:5'

#print urlmapa+'|'+str(latitud)+','+str(longitud)

while contadores != contador:
	variable=variable+'|'+str(listalatitud[contadores])+','+str(listalongitud[contadores])
	contadores=contadores+1
	
urlfinal=urlmapa+variable

print urlfinal	
	
#while contadores != contador:
	#contadores=contadores+1
	#print 'La lista de latitud: ',listalatitud[contadores]
	#print ''
	#print 'La lista de longitud: ',listalongitud[contadores]
	


# http://maps.googleapis.com/maps/api/staticmap?size=400x400&path=color:0x0000ff|weight:5|40.737102,-73.990318|40.749825,-73.987963|40.752946,-73.987384|40.755823,-73.986397


