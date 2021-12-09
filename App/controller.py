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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # analyzer es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones para la carga de datos

def loadData(catalog):
    """
    cargamos los datos a las estructuras ya creadas
    """
    loadAirports(catalog)
    loadVuelos(catalog)
    loadCity(catalog)


def loadAirports(analyzer):
    """
    Carga los artistas archivo.  .
    """
    airportsfile = cf.data_dir + 'Skylines/airports-utf8-large.csv'
    input_file = csv.DictReader(open(airportsfile, encoding='utf-8'))
    i=0
    for airport in input_file:
        if i==0:
            model.addAirport(analyzer, airport)
            model.printAirport(analyzer,airport,i)
            i=i+1
        elif i!=0:
            model.addAirport(analyzer,airport)
            i=i+1
    model.printAirport(analyzer,airport,i)
        

def loadVuelos(analyzer):
    """
    carga los vuelos 
    """
    
    Vuelosfile = cf.data_dir + 'Skylines/routes-utf8-large.csv'
    input_file = csv.DictReader(open(Vuelosfile, encoding='utf-8'))
 
    for vuelo in input_file:
    
        model.addVuelos(analyzer, vuelo)
            
      

        

def loadCity(analyzer):
    Cityfile = cf.data_dir + 'Skylines/worldcities-utf8.csv'
    input_file = csv.DictReader(open(Cityfile, encoding='utf-8'))
    i=0
    for city in input_file:
        if i==0:

            model.addCity(analyzer, city)
            model.printCity(analyzer,city,i)
            i=i+1
        elif i!=0:
            model.addCity(analyzer, city)
            i=i+1
    model.printCity(analyzer,city,i)





# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def AeroCerrado(catalog, cerrado):
    return model.AeroCerrado(catalog, cerrado)

def ComponentesFuertes(catalog, ae1, ae2):
    return model.ComponentesFuertes(catalog, ae1, ae2)

def viajeCiudades(catalog,city1,city2):
    return model.viajeCiudades(catalog,city1,city2)

def AeroInter(catalog):
    return model.AeroInter(catalog)

def Miles(InputCity,Miles,catalog):
    Miles=float(Miles)
    return model.Miles(InputCity,Miles,catalog)
