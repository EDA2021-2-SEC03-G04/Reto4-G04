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

catalog = None

"""
Funciones para imprimir 
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar: ')
    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        catalog = controller.init()
        print("\nCargando información....")
        controller.loadData(catalog)
        print("se cargo la informacion")
        


    elif int(inputs[0]) == 2:
        
        printEspacio()

        printEspacio()


    elif int(inputs[0]) == 3:
        
        printEspacio()

        printEspacio()

    
    elif int(inputs[0])==4:

        printEspacio()

        printEspacio()


    elif int(inputs[0])==5:

        printEspacio()
        
        printEspacio()


    elif int(inputs[0]) == 6:
        
        printEspacio()

        printEspacio() 
        

    else:
        sys.exit(0)
sys.exit(0)