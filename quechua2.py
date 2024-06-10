# -*- coding: utf-8 -*-

#leemos el excel
import streamlit as st
import pandas as pd

verbos = pd.read_excel ('verbos.xlsx')
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


pronombre = pd.read_excel('quechua.xlsx', sheet_name = 'pronombres')
col = pronombre.columns
pronombre.set_index(col[0], inplace=True)
d_pronombre = pronombre.to_dict()

#Diccionario de pronombres


#Función para conjugar verbos
def conjugador(base,persona,numero,tiempo):
  return d_pronombre[numero][persona] + ' ' + base + D[tiempo][numero][persona]

conjugador('miku','segunda','plural','presentesimple')



##diccionario

quechua = list(verbos['quechua'])
espanol = list(verbos['español'])

dict_que_esp = dict(zip(quechua,espanol))

##importamos streamlit



base = st.selectbox(
    
    "Seleccione un verbo en quechua",quechua)
st.write("El verbo en español es:", dict_que_esp[base])
if base.endswith("y"):
   base = base[:-1]




#para persona

persona = st.selectbox(
    "Seleccione una persona:",
    ["primera inclusiva","primera exclusiva","segunda","tercera"])
    
st.write("Seleccionaste:", persona)

#para tiempo
tiempo = st.selectbox(
    "Seleccione un tiempo:",
    ["presentesimple","presenteprogresivo", "presentehabitual", "pasadoexperimentadosimple", "pasadoexperimentadoprogresivo", "pasadoexperimentadohabitual", "pasadonoexperimentadosimple", "pasadonoexperimentadoprogresivo", "pasadonoexperimentadohabitual"])
st.write("Seleccionaste:", tiempo)
#para número

numero = st.selectbox(
    "Seleccione un número:",
    ["singular","plural"])

st.write("Seleccionaste:", numero)

st.write("El verbo conjugado es:", conjugador(base,persona,numero,tiempo))