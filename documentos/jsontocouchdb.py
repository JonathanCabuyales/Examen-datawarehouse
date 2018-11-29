# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import xlrd #libreria para leer archivos excel
from collections import OrderedDict
import simplejson as json
import couchdb
""" Conectamos a la base de datos """
user = "user"
password = "user"
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))
#VErificamos que exista la base de datos
#Sino la crea
dbname = "nba"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)
libro = xlrd.open_workbook('nba.xlsx')
hoja = libro.sheet_by_index(0)
#Recorremos el archiv excel fila por fila
try:
    for i in range(0, hoja.nrows):
        dato_lista = {}
        valores = hoja.row_values(i)
        dato_lista['nba'] = {
        'Active_season':valores[0],
        'Player':valores[1],
        'Team':valores[2],
        'Conference':valores[3],
        'Date':valores[4],
        'Position':valores[5],
        'Height':valores[6],
        'Weight':valores[7],
        'Age':valores[8],
        'Draft_Year':valores[9],
        'Season_in_league':valores[10],
        'Season':valores[11],
        'Season_short':valores[12],
        'Real_value':valores[13]
        }
        #Lo almacenamos en couchdb 
        doc_id, doc_rev = db.save(dato_lista)
except Exception as e:
    print("error"+e)

    """with open(str(i)+'.json', 'w') as file:
        json.dump(dato_lista, file, indent=4)"""

    

    




