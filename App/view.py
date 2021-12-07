"""
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
        print("los componetes no estan fuertemente conectados")

    print("")
    print("aereopuerto 1: ")
    aere1 = mp.get(catalog["airports"], ae1)["value"]
    print("El aereopuerto " + aere1["name"] + " con codigo " + ae1 + " de la ciudad " + aere1["city"] + " y del pais " + aere1["country"])

    print("")
    print("aereopuerto 2: ")
    aere2 = mp.get(catalog["airports"], ae2)["value"]
    print("El aereopuerto " + aere2["name"] + " con codigo " + ae2 + " de la ciudad " + aere2["city"] + " y del pais " + aere2["country"])



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
        
        printEspacio()


    elif int(inputs[0]) == 2:
        
        printEspacio()

        printEspacio()


    elif int(inputs[0]) == 3: #REQ2
        
        printEspacio()

        ae1 = input("Codigo IATA del aereopuerto 1(LED): ")
        ae2 = input("Codigo IATA del aereopuerto 2(RTP): ")
        print("")
        retorno = controller.ComponentesFuertes(catalog, ae1, ae2)

        printREQ2(retorno, ae1, ae2)

        printEspacio()

    
    elif int(inputs[0])==4:

        printEspacio()

        printEspacio()


    elif int(inputs[0])==5:

        printEspacio()
        
        printEspacio()


    elif int(inputs[0]) == 6: #REQ5
        
        printEspacio()

        cerrado = input("Cual es el aereopuerto cerrado(DXB): ")
        print("")

        retorno = controller.AeroCerrado(catalog, cerrado)

        printREQ6(retorno)

        printEspacio() 
        

    else:
        sys.exit(0)
sys.exit(0)