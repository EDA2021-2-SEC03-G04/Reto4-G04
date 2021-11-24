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


def loadAirports(analyzer):
    """
    Carga los artistas archivo.  .
    """
    airportsfile = cf.data_dir + 'Skylines/airports_full.csv'
    input_file = csv.DictReader(open(airportsfile, encoding='utf-8'))
    for airport in input_file:
        model.addAirport(analyzer, airport)


def loadVuelos(analyzer):
    """
    carga los vuelos 
    """
    Vuelosfile = cf.data_dir + 'Skylines/routes_full.csv'
    input_file = csv.DictReader(open(Vuelosfile, encoding='utf-8'))
    for vuelo in input_file:
        model.addVuelos(analyzer, vuelo)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

