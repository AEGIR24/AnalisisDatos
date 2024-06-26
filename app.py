import pandas as pd
import streamlit as st
from PIL import Image


st.title('Análisis de datos de Sensores en Mi Ciudad')
image = Image.open('grafana2.jpg')
st.image(image)

# Subida de archivo
uploaded_file = st.file_uploader('Selecciona tu archivo csv')

# Lectura del archivo
if uploaded_file is not None:
   df1=pd.read_csv(uploaded_file)

   # Parte grafica de los datos
   st.subheader('Perfil gráfico de la variable medida.')
   # Para la variable tiempo
   df1 = df1.set_index('time')
   # Representacion grafica lineal del tiempo
   st.line_chart(df1)
   
   st.write(df1)
   st.subheader('Estadísticos básicos de los sensores.')
   st.dataframe(df1["temperatura"].describe())
   
   min_temp = st.slider('Selecciona valor mínimo del filtro ', min_value=-10, max_value=45, value=23, key=1)
   # Filtrar el DataFrame utilizando query
   filtrado_df_min = df1.query(f"`temperatura` > {min_temp}")
   # Mostrar el DataFrame filtrado

   
   st.subheader("Temperaturas superiores al valor configurado.")
   st.write('Dataframe Filtrado')
   
   st.write(filtrado_df_min)
   
   max_temp = st.slider('Selecciona valor máximo del filtro ', min_value=-10, max_value=45, value=23, key=2)
   # Filtrar el DataFrame utilizando query
   filtrado_df_max = df1.query(f"`temperatura` < {max_temp}")
   # Mostrar el DataFrame filtrado

   
   st.subheader("Temperaturas Inferiores al valor configurado.")
   st.write('Dataframe Filtrado')
   
   st.write(filtrado_df_max)
   

else:
 st.warning('Necesitas cargar un archivo csv excel.')
