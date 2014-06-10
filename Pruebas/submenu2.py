#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import json
import bottle


origen=raw_input('Seleccione la ciudad origen: ')
destino=raw_input('Seleccione la ciudad destino: ')
listadistancia=['']
listaduration=['']
listahtml=['']

url='http://maps.googleapis.com/maps/api/directions/json'
obtener=requests.get(url=url,params={'origin':origen,
									   'destination':destino,
									   'region':'ES',
									   'sensor':'false',
									   'avoid':'highways',
									   'units':'metric',
									   'mode':'BUS'})


dicc = json.loads(obtener.text.encode("utf-8"))

contador=0
contadores=[]

for i in dicc['routes'][0]['legs'][0]['steps']:
	distancia= i['distance']['text']
	duration= i['duration']['text']
	html=i['html_instructions']
	listadistancia.append(distancia)
	listaduration.append(duration)
	listahtml.append(html)
	contador=contador+1
	contadores.append(contador)
	#print contador


		
for i in contadores:
	print 'La distancia es: '+listadistancia[i]
	print 'La duracion es: '+listaduration[i]
	print 'Instruccion: '+listahtml[i]
	print '				'
	
print 'Ha llegado a su destino'
