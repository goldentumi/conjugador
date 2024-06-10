# -*- coding: utf-8 -*-


#Tablas de conjugación en excel
import pandas as pd
quechua = pd.read_excel('quechua.xlsx')

#Abrir todas las hojas del excel
excel_file = pd.ExcelFile('quechua.xlsx')
D = {}
for hoja in excel_file.sheet_names:
  df = pd.read_excel('quechua.xlsx', sheet_name = hoja)
  c = df.columns
  df.set_index(c[0], inplace = True)
  print(f'Hoja: {hoja}')
  print(df.head())

  d = df.to_dict()

  D[hoja] = d

#Diccionario
D

pronombre = pd.read_excel('quechua.xlsx', sheet_name = 'pronombres')
col = pronombre.columns
pronombre.set_index(col[0], inplace=True)
d_pronombre = pronombre.to_dict()

#Diccionario de pronombres
d_pronombre

#Función para conjugar verbos
def conjugador(base,persona,numero,tiempo):
  return d_pronombre[numero][persona] + ' ' + base + D[tiempo][numero][persona]

conjugador('miku','segunda','plural','presentesimple')

#Para ingresar más fácilmente las condiciones
base = input('Ingrese base aquí:')
persona= input('Ingrese persona (diferencia primera incl / excl):')
numero = input('Ingrese número (singular / plural):')
tiempo = input('Ingrese tiempo (sinespacios):')

conjugador(base,persona,numero,tiempo)