"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.ADT import map as m
from DISClib.ADT.graph import gr
from DISClib.Utils import error as error
assert cf
import math

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newAnalyzer():
    """ Inicializa el analizador

   stops: Tabla de hash para guardar los vertices del grafo
   GRAPH: Grafo para representar las rutas entre estaciones
   components: Almacena la informacion de los componentes conectados
   paths: Estructura que almancena los caminos de costo minimo desde un
           vertice determinado a todos los otros vértices del grafo
    """
    try:
        analyzer = {
                    'airports': None,
                    'GRAPHD': None,
                    'components': None,
                    'paths': None,
                    'GRAPHND': None
                    }

        analyzer['airports'] = m.newMap(numelements=90076,
                                     maptype='CHAINING',
                                     comparefunction=compareIATA)

        analyzer['GRAPHD'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=92606,
                                              comparefunction=compareIATA)

        analyzer['GRAPHND'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=False,
                                              size=92606,
                                              comparefunction=compareIATA)

                                           
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')


# Funciones para agregar informacion al catalogo

def addAirport(analyzer,airport):

    IATA=str(airport['IATA'])
    new=newAirport(airport['Name'],airport['City'],airport['Country'],airport['Latitude'],airport['Longitude'])
    
    
    #Añade el vertice IATA al GRAPHD
    GRAPHD=analyzer['GRAPHD']
    if not( gr.containsVertex(GRAPHD,IATA)):
        gr.insertVertex(GRAPHD,IATA)
    #Añade el vertice IATA al hashmap airports
    airports=analyzer['airports']
    if not( mp.contains(airports,IATA)):
        mp.put(airports,IATA,new)

    #Añadir info al No dirigido
    GRAPHND=analyzer['GRAPHND']
    if not( gr.containsVertex(GRAPHND,IATA)):
        gr.insertVertex(GRAPHND,IATA)
    
    

        
def addVuelos(analyzer, vuelo):

    #sacamos valores
    inicio = str(vuelo["Departure"])
    fin = str(vuelo["Destination"])
    distancia = vuelo["distance_km"]
    GRAPHD=analyzer['GRAPHD']
    GRAPHND=analyzer['GRAPHND']
    distancia=int(math.floor(float(distancia)))
    


    #añadimos valores al dirigido
    if gr.getEdge(GRAPHD, inicio, inicio) != None:
        gr.addEdge(GRAPHD, inicio, fin, distancia)
    

    #si exsiste la relacion anterior en sentido contrario se agrega al no dirigido
    if gr.getEdge(GRAPHD, fin, inicio) != None:
        gr.addEdge(GRAPHND, inicio, fin, distancia)


# Funciones para creacion de datos

def newAirport(name,city,country,latitude,longitude):

    airport={'name':name,'city':city,'country':country,'latitude':latitude,'longitude':longitude}

    return airport

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista


# ==============================
# Funciones de Comparacion
# ==============================


def compareIATA(iata1, iata2):
    """
    Compara dos estaciones
    """
    
    iata2=iata2['key']
    

    if (iata1 == iata2):
        return 0
    elif (iata1 > iata2):
        return 1
    else:
        return -1


# Funciones de ordenamiento
