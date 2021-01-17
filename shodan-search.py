#!/usr/local/bin/python3
#-*- coding: utf-8 -*-

#Autor: José Moreno
#Fecha: 17/04/21
#Descripción: script para recopilar resultados de shodan, modificado de opensec
#contacto: jam620@protonmail.com

import shodan
#ingresa la key de shodan
SHODAN_API_KEY = ""

api = shodan.Shodan(SHODAN_API_KEY)

while 1:
    query = input("Ingrese su query: ")
    if query.strip() == 'end':
        break

    try:
       results = api.search(query)
       # Show the results
       print ("Results found ---> %s{}".format(results['total']))
       resultado = 1
       for result in results['matches']:
           print ("Resultado Numero %s{}".format(result))
           #podemos añadir los campos de shodan cli
           print ("IP ---> %s{}".format(result['ip_str']))
           print("Port ---> %s{}".format(result['port']))
           '''Comente la linea 29 para que no me devuelva todo el cuerpo'''
           #print ("Banner --->\n %s{}".format(result['data']))
           print ()
           resultado += 1
    except shodan.APIError as e:
           print ("Error: %s{}".format(e))
