# -*- coding: utf-8 -*-

#leemos el excel
import streamlit as st
import pandas as pd

def color_de_fondo():
    st.markdown(
        f'''
         <style>
         .stApp {{
             background-color: #FFE3E8;
             }}
         </style>
         ''',
         unsafe_allow_html=True
         )

color_de_fondo()

st.title(':rainbow[Conjugador de verbos en quechua]')


verbos = pd.read_excel ('verbos.xlsx', sheet_name='Hoja 1')
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
    
    ":violet-background[Seleccione un verbo en quechua]",quechua)
st.write("El verbo en español es:", dict_que_esp[base])
if base.endswith("y"):
   base = base[:-1]




#para persona

persona = st.selectbox(
    "Seleccione una persona:",
    ["primera inclusiva","primera exclusiva","segunda","tercera"])
 

with st.popover("¿Por qué hay dos opciones para primera persona?"):
    st.markdown('''En quechua, el plural de primera persona distingue entre inclusiva y exclusiva.  
                :green[**Inclusiva:**] todos nosotros   
                :green[**Exclusiva:**] nosotros (tú y yo)''')
    

st.write("Seleccionaste:", persona)

#diccionario de tiempos

#para tiempo
tiempo = st.selectbox(
    "Seleccione un tiempo:",
    ["presentesimple","presenteprogresivo", "presentehabitual", "pasadoexperimentadosimple", "pasadoexperimentadoprogresivo", "pasadoexperimentadohabitual", "pasadonoexperimentadosimple", "pasadonoexperimentadoprogresivo", "pasadonoexperimentadohabitual"])
st.write("Seleccionaste:", tiempo)
d_tiempo = {'presentesimple':'El **presente simple** es equivalente a las formas castellanas *yo como; tú bailas,* etc. En quechua, el presente simple es el tiempo no marcado, es decir que no hay una marca explícita que indique tal tiempo; por el contrario, para conjugar un verbo en presente simple solo es necesario añadir las marcas personales a la raíz verbal.','presenteprogresivo':'Llamamos **presente progresivo** a la forma del presente equivalente a las perífrasis verbales castellanas *estoy comiendo* o *estoy bailando*. Es decir que el presente progresivo se emplea cuando el **evento descrito por una oración está ocurriendo mientras dicha oración es pronunciada**. En otras palabras, el presente progresivo se emplea cuando el evento referido por la oración es simultáneo al acto de habla. Para conjugar verbos en presente progresivo solo es necesario anteponer el sufijo **-chka** a las marcas personales del presente simple.','presentehabitual': 'Llamamos **presente habitual** a la forma del presente equivalente a las perífrasis verbales castellanas *suelo caminar* o *suelo hablar*. Es decir que el presente habitual se emplea cuando el **evento descrito por una oración es cotidiano, natural y se da con cierta regularidad**. Para conjugar verbos en presente habitual es necesario hacer uso de una perífrasis verbal, en la que añadiremos el sufijo **–q** al verbo principal y emplearemos el verbo ser, **kay**, conjugado en presente simple, a manera de auxiliar. Como puedes apreciar, en el caso de la :blue[**tercera persona no se debe incluir el verbo ser, sino que es suficiente con el sufijo –mi**], tal como ocurría con el presente simple.','pasadoexperimentadosimple': 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo **pasado experimentado**, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** antes de la marca de persona.','pasadoexperimentadoprogresivo' : 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo pasado experimentado, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** después de la marca de progresivo y antes de la marca de persona.','pasadoexperimentadohabitual' : 'Esta forma de pasado se emplea cuando narramos hechos de los cuales hemos sido :blue[**testigos directos**]; es decir, hechos que nos constan. Por este valor, las distintas gramáticas quechuas llaman a este tiempo pasado experimentado, ya que lo que se está indicando es que el hablante ha experimentado lo que está diciendo. Se conjuga agregando el sufijo **-rqa** en el verbo **kay**, antes de la marca de persona.','pasadonoexperimentadosimple': 'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**.','pasadonoexperimentadoprogresivo' :	'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**. Se conjuga agregando dicho sufijo después de la marca de progresivo y antes de la marca de persona.','pasadonoexperimentadohabitual':	'El sufijo **–sqa** se emplea cuando se quiere hablar de hechos de los cuales :blue[**no hemos sido testigos directos**]; es decir hechos sobre los cuales no estamos seguros porque no nos constan. Este tiempo se usa, por ejemplo, para **contar mitos, cuentos, chistes y leyendas**. Se conjuga agregando dicho sufijo al verbo **kay**, antes de la marca de persona.'}
with st.popover ("Da click aquí para conocer más sobre los tiempos."):
    st.markdown(d_tiempo[tiempo])
#para número

numero = st.selectbox(
    "Seleccione un número:",
    ["singular","plural"])

st.write("Seleccionaste:", numero)

st.write("El verbo conjugado es:", conjugador(base,persona,numero,tiempo))