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
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Algorithms.Sorting import mergesort as mrgsort
from DISClib.Algorithms.Graphs import prim as prim
from DISClib.ADT import queue as que
from DISClib.Algorithms.Graphs import bellmanford as bellman
from DISClib.ADT import stack
from DISClib.ADT import map as m
from DISClib.ADT.graph import gr
from DISClib.Utils import error as error
assert cf
import math
from math import radians, cos, sin, asin, sqrt

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
                    'GRAPHND': None,
                    "city":None
                    }

        analyzer['airports'] = m.newMap(numelements=90076,
                                     maptype='CHAINING',
                                     comparefunction=compareIATA)

        analyzer['airportsByCity'] = m.newMap(numelements=90076,
                                     maptype='CHAINING',
                                     comparefunction=compareIATA)

        analyzer['cityCant'] = m.newMap(numelements=41076,
                                     maptype='CHAINING',
                                     )

        analyzer['cityList'] = m.newMap(numelements=41076,
                                     maptype='CHAINING',
                                     )

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
    new=newAirport(airport['Name'],airport['City'],airport['Country'],airport['Latitude'],airport['Longitude'], airport['IATA'])
    city=airport['City']
    
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

    if mp.contains( analyzer['airportsByCity'], city):
        old=mp.get(analyzer["airportsByCity"], city)["value"]
        lt.addLast(old, new)
        mp.put(analyzer["airportsByCity"], city, old)
    else:
        nuevo=lt.newList()
        lt.addLast(nuevo, new)
        mp.put(analyzer["airportsByCity"],  city, nuevo)
    
    

        
def addVuelos(analyzer, vuelo):

    #sacamos valores
    inicio = str(vuelo["Departure"])
    fin = str(vuelo["Destination"])
    distancia = vuelo["distance_km"]
    GRAPHD=analyzer['GRAPHD']
    GRAPHND=analyzer['GRAPHND']
    distancia=int(math.floor(float(distancia)))
    


    #añadimos valores al dirigido
    
    gr.addEdge(GRAPHD, inicio, fin, distancia)
    

    #si exsiste la relacion anterior en sentido contrario se agrega al no dirigido
    if gr.getEdge(GRAPHD, fin, inicio) != None:
        gr.addEdge(GRAPHND, inicio, fin, distancia)


def addCity(analyzer, city):

    
    new={"city":city["city"], "country":city["country"], "lat":city["lat"], "lng":city["lng"], "population":city["population"]}
    key=city["city"]
    key2=key
    
    
    repes=0

    while mp.contains(analyzer["cityCant"], key2):
        repes+=1
        key2=key2+str(repes)
    
    nuevo=lt.newList()
    lt.addLast(nuevo, new)
    mp.put(analyzer["cityCant"],  key2, nuevo)

    #Dos formas

    if mp.contains(analyzer["cityList"], key):
        old=mp.get(analyzer["cityList"], key)["value"]
        lt.addLast(old, new)
        mp.put(analyzer["cityList"], key, old)
    else:
        nuevo=lt.newList()
        lt.addLast(nuevo, new)
        mp.put(analyzer["cityList"],  key, nuevo)


# Funciones para creacion de datos

def newAirport(name,city,country,latitude,longitude,IATA):

    airport={'name':name,'city':city,'country':country,'latitude':latitude,'longitude':longitude, "IATA":IATA}

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

def AeroCerrado(catalog, cerrado):
    
    principal = catalog["GRAPHD"]

    retorno1 = gr.adjacents(principal, cerrado)
    retorno2 = gr.degree(principal, cerrado)

    return [retorno1, retorno2]

def ComponentesFuertes(catalog, ae1, ae2):
    principal = catalog["GRAPHD"]
    kosa = scc.KosarajuSCC(principal)
    cantidad = scc.connectedComponents(kosa)

    conectados = scc.stronglyConnected(kosa, ae1, ae2)

    return[cantidad, conectados]

def viajeCiudades(catalog,city1,city2):
    #determinar ciudad

    principal = catalog["cityList"]
    Aereopuertos = catalog["airportsByCity"]
    grafo = catalog["GRAPHD"]

    listaC1 = mp.get(principal, city1)["value"]
    listaC2 = mp.get(principal, city2)["value"]

    C1 = None
    C2 = None

    if lt.size(listaC1) >1:
        print("Encontramos ciudades omonimas")
        print("")
        
        for x in range(lt.size(listaC1)):
            elemento = lt.getElement(listaC1, x+1)
            print(str(x+1)+ ")" + elemento["city"] + " en " + elemento["country"] + " con latitud " +  elemento["lat"] + " y longitud " +  elemento["lng"])
            print("")

        posi = int(input("Elige 1: "))
        print("")

        C1 = lt.getElement(listaC1, posi)
    else:
        C1 = lt.getElement(listaC1, 1)

    if lt.size(listaC2) >1:
        print("Encontramos ciudades omonimas")
        print("")
        
        for x in range(lt.size(listaC2)):
            elemento = lt.getElement(listaC2, x+1)
            print(str(x+1)+ ")" + elemento["city"] + " en " + elemento["country"] + " con latitud " +  elemento["lat"] + " y longitud " +  elemento["lng"])
            print("")

        posi = int(input("Elige 1: "))
        print("")

        C2 = lt.getElement(listaC2, posi)
    else:
        C2 = lt.getElement(listaC2, 1)


    C1Aereo = mp.get(Aereopuertos,C1["city"])["value"]
    C2Aereo = mp.get(Aereopuertos,C2["city"])["value"]

    salida = None
    llegada = None

    #para ciudad 1

    if lt.size(C1Aereo) > 1:
        
        val = []
        for x in range(lt.size(C1Aereo)):
            aereo = lt.getElement(C1Aereo, x+1)
            latAE = aereo["latitude"]
            longAE = aereo["longitude"]
            latC1 = C1["lat"]
            longC1 = C1["lng"]
            dist = haversine(float(longAE), float(latAE), float(longC1), float(latC1))
            val.append(dist)

        minimo = min(val)

        posi = val.index(minimo) 

        salida = lt.getElement(C1Aereo, posi)
    else:
        salida = lt.getElement(C1Aereo, 1)

    #para ciudad 2

    if lt.size(C2Aereo) > 1:
        
        val = []
        for x in range(lt.size(C2Aereo)):
            aereo = lt.getElement(C2Aereo, x+1)
            latAE = aereo["latitude"]
            longAE = aereo["longitude"]
            latC2 = C2["lat"]
            longC2 = C2["lng"]
            dist = haversine(float(longAE), float(latAE), float(longC2), float(latC2))
            val.append(dist)

        minimo = min(val)

        posi = val.index(minimo) + 1

        llegada = lt.getElement(C2Aereo, posi)
    else:
        llegada = lt.getElement(C2Aereo, 1)


    caminos = djk.Dijkstra(grafo, salida["IATA"])
    ruta = djk.pathTo(caminos, llegada["IATA"])

    return [ruta, salida, llegada]

    """
    if ruta is not None:
        
        while (not stack.isEmpty(ruta)):
            stop = stack.pop(ruta)
            print(stop)

    else:
        print('No hay camino')
    """

def AeroInter(catalog): 
    '''
    Funcion que calcula el top 5 aeropuertos más interconectados
    '''
    #Toma el grafo dirigido
    Graph=catalog['GRAPHD']
    #Saca la lista de vertices 
    VertexList=gr.vertices(Graph)
    #Crea una lista vacía para guardar el top 5
    ConnectedList=lt.newList()
    #Contador para ir calculando el top 5
    Top=0
    #Recorre todos los vertices
    for vertex in lt.iterator(VertexList):
        #Calcula el degree de cada vertice
        VertexDegree=gr.degree(Graph,vertex)

        #Va guardando y actualizando el top5
        if VertexDegree>Top:
            #Saca la info necesaria para imprimir en consola
            Indegree=gr.indegree(Graph,vertex)
            Outdegree=gr.outdegree(Graph,vertex)
            ElementInfo=mp.get(catalog['airports'],vertex)['value']
            Name=ElementInfo['name']
            City=ElementInfo['city']
            Country=ElementInfo['country']
            New={'vertex':vertex,'degree': VertexDegree,'name':Name,'city':City,'country':Country,'indegree':Indegree,'outdegree':Outdegree}
            #Lo añade al top 5
            lt.addLast(ConnectedList,New)
            Top=VertexDegree

    #Sortea la lista de top 5 
    mrgsort.sort(ConnectedList,cmpByDegree)
    return ConnectedList    

def Miles(InputCity,Miles,catalog):
    '''
    Funcion que saca la rama más larga de el MST con raíz InputCity
    '''
    #Toma el grafo dirigido y el hashmap de la info de ciudades
    Graph=catalog['GRAPHND']
    CityInfoMap=catalog['airports']
    #Calcula un MST
    MST=prim.PrimMST(Graph)

    #Saca la suma de los costos de todos los arcos del MST
    MSTCost=prim.weightMST(Graph,MST)
    #Saca el tamaño del MST
    NumVertex=que.size(MST['mst'])
    #Saca la info de la ciudad de input
    Info=mp.get(CityInfoMap,InputCity)['value']
    #Va viendo cuál es la rama más larga
    longest=0

    #Calcula el algoritmo de Dijkstra para la input city
    #Bellman=bellman.BellmanFord(Graph,InputCity)
    Dijk=djk.Dijkstra(Graph,InputCity)
    Route=None

    #Recorre todos los nodos del MST 
    for Element in range(int(NumVertex)):
        Element=que.dequeue(MST['mst'])
       
        In=Element['vertexA']
        
        #Calcula la mínima distancia entre la ciudad de input y el nodo del MST

        #dist=bellman.distTo(Bellman,In)
        dist=djk.distTo(Dijk,In)
        
        #print(dist>longest)
        #if  dist > longest and dist !=float('inf') and bellman.pathTo(Bellman,In) != None:
            #print('entré')
            #print(dist)
            #Route=In
            #longest=dist
        #Va actualizando la rama más larga y si sí pertenece al MST
        if  dist > longest and dist !=float('inf') and djk.pathTo(Dijk,In) != None:
            
            Route=In
            longest=dist
    
    #route=bellman.pathTo(Bellman,Route)

    #Calcula la ruta final
    route=djk.pathTo(Dijk,Route)
    #print(Route)
    #print(bellman.distTo(Bellman,Route))
    #print(route)



    return MSTCost,Info,NumVertex,route



def cmpByDegree(vertex1,vertex2):

    degree1=vertex1['degree']
    degree2=vertex2['degree']

    return degree2<degree1


































def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    Fuente: https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r