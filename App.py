import streamlit as st
st.title('titulo')

col1,col2,col3 =st.columns([4,4,6])

if col1.button('gatos'):
  st.image('https://www.mascotasmania.es/wp-content/uploads/2022/08/nombres-para-gatos-negros.jpg')
if col2.button('perros'):
  st.image('https://www.fundacion-affinity.org/sites/default/files/los-10-sonidos-principales-del-perro.jpg')
if col3.button('patos'):
  st.image('https://quo.eldiario.es/wp-content/uploads/2019/10/por-que-los-patos-tienen-las-patas-naranja.jpg')

col1.write('este mensaje aparece solamente en la primera columna')

col2.header('Este es un encabezado en la segunda columna')

col3.image('https://www.mascotasmania.es/wp-content/uploads/2022/08/nombres-para-gatos-negros.jpg')
