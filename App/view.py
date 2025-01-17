﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT.graph import gr
from DISClib.ADT import map as mp
from DISClib.ADT import stack
assert cf
import time


default_limit=10000
sys.setrecursionlimit(default_limit*10)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2-(REQ1)  Encontrar puntos de interconexión aérea ")
    print("3-(REQ2)  Encontrar clústeres de tráfico aéreo ")
    print("4-(REQ3)  Encontrar la ruta más corta entre ciudades ")
    print('5-(REQ4)  Utilizar las millas de viajero ')
    print('6-(REQ5)  Cuantificar el efecto de un aeropuerto cerrado ')
    print('7-(BONO)  Comparar con servicio WEB externo ')


def printEspacio():
    """
    añade espacios entre funciones 
    """

    print("")
    print("=" * 100)
    print("")


def printREQ1(retorno):

    print()

    print('Top 5 aeropuertos más interconectados: ')
    print()
    x=0
    for Element in lt.iterator(retorno):
        if x <5:
            x=x+1
            print(str(x) + ')  Nombre: ' + str(Element['name']) + '   Ciudad: ' + str(Element['city']) + '   País: ' + str(Element['country']) + '   IATA: ' + str(Element['vertex']) + '   Conexiones: ' + str(Element['degree']) + '   Inbound: ' + str(Element['indegree']) + '   Outbound: ' + str(Element['outdegree']))


def printREQ6(retorno):
    aereo = retorno[0]
    rutas = retorno[1]

    print("Si se cierra este aereopurto se afectan " + str(lt.size(aereo)) + " aereopuertos y " + str(rutas) + " rutas")

    print()

    print("El top 3 primeros: ")

    for x in range(3):
        codigo = lt.getElement(aereo, x+1) 
        aere = mp.get(catalog["airports"], codigo)["value"]
        print("El aereopuerto " + aere["name"] + " con codigo " + codigo + " de la ciudad " + aere["city"] + " y del pais " + aere["country"])

    print("El top 3 ultimos: ")

    for x in range(3):
        codigo = lt.getElement(aereo, lt.size(aereo)-x) 
        aere = mp.get(catalog["airports"], codigo)["value"]
        print("El aereopuerto " + aere["name"] + " con codigo " + codigo + " de la ciudad " + aere["city"] + " y del pais " + aere["country"])

def printREQ2(retorno, ae1, ae2):

    print("Existen " + str(retorno[0]) + " css")
    if retorno[1]:
        print("Los aereopuertos estan fuertemente conectados")
    else:
        print("los aereopuertos no estan fuertemente conectados")

    print("")
    print("aereopuerto 1: ")
    aere1 = mp.get(catalog["airports"], ae1)["value"]
    print("El aereopuerto " + aere1["name"] + " con codigo " + ae1 + " de la ciudad " + aere1["city"] + " y del pais " + aere1["country"])

    print("")
    print("aereopuerto 2: ")
    aere2 = mp.get(catalog["airports"], ae2)["value"]
    print("El aereopuerto " + aere2["name"] + " con codigo " + ae2 + " de la ciudad " + aere2["city"] + " y del pais " + aere2["country"])

def printREQ3(retorno, city1, city2):

    print("De " + city1 + " hasta " + city2)
    print("")

    aere1 = retorno[1]
    print("El aereopuerto de salida es: ")
    print("El aereopuerto " + aere1["name"] + " con codigo " + aere1["IATA"] + " de la ciudad " + aere1["city"] + " y del pais " + aere1["country"])
    print("")


    aere2 = retorno[2]
    print("El aereopuerto de llegada es: ")
    print("El aereopuerto " + aere2["name"] + " con codigo " + aere2["IATA"] + " de la ciudad " + aere2["city"] + " y del pais " + aere2["country"])
    print("")

    print("El camino es: ")
    print("")

    ruta = retorno[0]
    intermedios = lt.newList()

    if ruta is not None:
        
        while (not stack.isEmpty(ruta)):
            arco = stack.pop(ruta)
            print("Desde " + arco["vertexA"] + " hasta " + arco["vertexB"] + " con una distancia de " + str(arco["weight"]))
            lt.addLast(intermedios, arco["vertexB"])

    lt.removeLast(intermedios)

    print("")
    print("Los pasos intermedios son: ")

    for x in range(lt.size(intermedios)):
        elemento = lt.getElement(intermedios, x+1)
        info = mp.get(catalog["airports"], elemento)["value"]
        print("El aereopuerto " + info["name"] + " con codigo " + elemento + " de la ciudad " + info["city"] + " y del pais " + info["country"])
    
def printREQ4(MSTCost,Info,InputCity,Miles,NumVertex,route):
    print()
    print('Información de ciudad de partida: ')
    print()
    print('IATA:  ' + str(InputCity) + '  Nombre:  ' + str(Info['name']) +  '  Ciudad:  ' + str(Info['city']) +  '  País:  ' + str(Info['country']))
    print()
    print('Número de posibles aeropuertos:    ' + str(NumVertex))
    print()
    print('Suma de distancias de posibles aeropurtos :  ' + str(MSTCost) + '  Km')
    print()
    print('Millas disponibles del viajero :' + str(float(Miles)*1.6) +  '  Km')

    print('-'*80)
    print()
    print('La ruta (rama más larga del MST) más larga posible desde ' + str(InputCity) + '  es: ')
    
    i=0
    tot=0
    
    for element in lt.iterator(route):
        print(str(i) + ')  '+ ' Desde  ' + str(element['vertexA']) + '  hacia:  ' + str(element['vertexB']) +  '  con distancia  ' +  str(element['weight']) + '  km')
        tot=tot+float(element['weight'])
        i=i+1
    print()
    print()
    print('Esta ruta tiene una distancia (ida y vuelta) de: ' + str(tot*2) + 'km')
    print()
    if float(Miles)*1.6  >= tot*2:
        print('El viajero tiene millas suficientes')
    else:
        print('A el viajero le hacen falta  ' +  str(abs(tot*2-float(Miles)*1.6)) + 'km  para poder hacer el viaje ')



"""
Funciones para imprimir 
"""

catalog = None

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:

        printEspacio()

        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        catalog = controller.init()
        print("\nCargando información....")
        controller.loadData(catalog)
        print("")
        print("se cargo la informacion")

        print("DiGrafo: ")
        print("")
        print("Aereopuetos: " + str(gr.numVertices(catalog["GRAPHD"])) )
        print("Rutas: " + str(gr.numEdges(catalog["GRAPHD"])))

        print("")

        print("Grafo: ")
        print("")
        print("Aereopuetos: " + str(gr.numVertices(catalog["GRAPHND"])) )
        print("Rutas: " + str(gr.numEdges(catalog["GRAPHND"])))

        print("")

        print("ciudades: ")
        print("")
        print("cantidad: " + str(mp.size(catalog["cityCant"])) )
        
        printEspacio()


    elif int(inputs[0]) == 2: #REQ1
        
        printEspacio()
        print('='*50 + 'RESPUESTA REQ1' + '='*50)

        StartTime=time.process_time()
        retorno=controller.AeroInter(catalog)
        StopTime=time.process_time()
        TimeMseg=(StopTime-StartTime)*1000
        print()
        print(f'El REQ tardó {TimeMseg} miliseg')

        printREQ1(retorno)

        printEspacio()


    elif int(inputs[0]) == 3: #REQ2
        
        printEspacio()

        ae1 = input("Codigo IATA del aereopuerto 1(LED): ")
        ae2 = input("Codigo IATA del aereopuerto 2(RTP): ")
        print("")

        StartTime=time.process_time()
        retorno = controller.ComponentesFuertes(catalog, ae1, ae2)
        StopTime=time.process_time()
        TimeMseg=(StopTime-StartTime)*1000
        print()
        print(f'El REQ tardó {TimeMseg} miliseg')


        print('='*50 + 'RESPUESTA REQ2' + '='*50)

        printREQ2(retorno, ae1, ae2)

        printEspacio()

    
    elif int(inputs[0])==4: #REQ3

        printEspacio()

        city1 = input("Ciudad de salida(St. Petersburg): ")
        city2 = input("Ciudad llegada(Lisbon): ")
        print("")

        StartTime=time.process_time()
        retorno = controller.viajeCiudades(catalog,city1,city2)
        StopTime=time.process_time()
        TimeMseg=(StopTime-StartTime)*1000
        print()
        print(f'El REQ tardó {TimeMseg} miliseg')

        print("")

        print('='*50 + 'RESPUESTA REQ3' + '='*50)

        printREQ3(retorno, city1, city2)

        printEspacio()


    elif int(inputs[0])==5: #REQ4

        printEspacio()
        InputCity=input('Ingrese el código IATA de la ciudad de origen(LIS): ')
        print()
        Miles=input('Ingrese la cantidad de millas disponibles(19850.0):  ')

        StartTime=time.process_time()
        MSTCost,Info,NumVertex,route=controller.Miles(InputCity,Miles,catalog)
        StopTime=time.process_time()
        TimeMseg=(StopTime-StartTime)*1000
        print()
        print(f'El REQ tardó {TimeMseg} miliseg')

        print('='*50 + 'RESPUESTA REQ4' + '='*50)
        printREQ4(MSTCost,Info,InputCity,Miles,NumVertex,route)

        
        printEspacio()


    elif int(inputs[0]) == 6: #REQ5
        
        printEspacio()

        cerrado = input("Cual es el aereopuerto cerrado(DXB): ")
        print("")

        StartTime=time.process_time()
        retorno = controller.AeroCerrado(catalog, cerrado)
        StopTime=time.process_time()
        TimeMseg=(StopTime-StartTime)*1000
        print()
        print(f'El REQ tardó {TimeMseg} miliseg')

        print('='*50 + 'RESPUESTA REQ5' + '='*50)
        printREQ6(retorno)

        printEspacio() 
        

    else:
        sys.exit(0)
sys.exit(0)