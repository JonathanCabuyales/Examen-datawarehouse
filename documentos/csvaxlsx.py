# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
import csv
import sys
# librerias para importar a couchdb desde archiv excel transformando a json
import xlrd
from collections import OrderedDict
import json
import couchdb

# credenciales para permitir el acceso a couchdb
user = "user"
password = "user"

couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))



# conversion de .csv a xlsx
from openpyxl import Workbook
if __name__ == '__main__':
    libro = Workbook()
    hoja = libro.active
    # abirmos el archivo en extension .csv y lo leeemos
    with open('nfl.csv', 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                for idx, val in enumerate(col.split(',')):
                    cell = hoja.cell(row=r + 1, column=c + 1)
                    cell.value = val
    libro.save('nfl.xlsx')

# importar de excel a couchdb
archivo = "nfl.xlsx"
# verificar a base de datos
dbname = "nfl"
if dbname in couchserver:
    db = couchserver[dbname]
else:
    db = couchserver.create(dbname)
libro = xlrd.open_workbook(archivo)
hoja =libro.sheet_by_index(0)
try:
    for i in range(0, hoja.nrows):
        lista = {}
        valores = hoja.row_values(i)
        lista['nfl'] = {
        'year': valores[0],
        'name':valores[1],
        'position': valores[4],
        'heightfeet':valores[5],
        'weight': valores[8],
        'fortyyd':valores[11],
        'twentyss': valores[14],
        'vertical':valores[16],
        'broad': valores[17],
        'bench':valores[18],
        'College': valores[20],
        'nflgrade':valores[25]

        }
        doc_id, doc_rev = db.save(lista)
except Exception as e:
    print("Error")
