import streamlit as st
import pandas as pd
st.title("Nutriva")

st.sidebar.title("La Alimentación")
st.sidebar.write("Casi una de cada tres personas en el mundo (2 370 millones) no tuvo acceso a una alimentación adecuada en 2020, lo que representa un aumento de casi 320 millones de personas en solo un año. La brecha de género con respecto a la prevalencia de inseguridad alimentaria moderada o severa ha aumentado debido a la pandemia.")
st.sidebar.image("https://viaorganica.org/wp-content/uploads/Image31291.gif")
st.sidebar.write("Integrantes:")
st.sidebar.write("Yocline  González")
st.sidebar.write("Andrea Daniela Morales Chávez")
st.sidebar.write("Estefania Acosta Dueñas ")
st.sidebar.write("Juan Pablo Vazquez Ortíz")

col1,col2,col3 =st.columns([4,4,4])

col1.subheader('Agua')
col1.image("https://static.vecteezy.com/system/resources/previews/003/823/823/non_2x/water-drop-cartoon-with-pointing-left-gesture-vector.jpg")
peso=col1.slider("Ingrese su peso en Kg",40,130,60)
vasos=(peso/7)*0.250 
x = round(vasos,3)
col1.write("su consumo apropiado de agua en litros al día es: ")
col1.write(x)

col2.subheader('Calorias por día')
col2.image("https://static.vecteezy.com/system/resources/previews/002/164/915/non_2x/reduce-calories-rgb-color-icon-vector.jpg")

estatura=col2.number_input("Ingrese su estatura en cm",120)
Edad=col2.slider("Ingrese su edad",10,90,17)
Femenino=655.1+(9.56*peso)+((1.85*estatura)-(4.65*Edad))
Masculino=65.5+(13.75*peso)+((5.08*estatura)-(6.78*Edad))
calorias2=Femenino*0.35
calorias02=Masculino*0.35
calorias3=Femenino*0.10
calorias03=Masculino*0.10
col2.write("Mujer (Kcal por día)")
col2.write(Femenino+calorias2+calorias3)
col2.write("Hombre (Kcal por día)")
col2.write(Masculino+calorias02+calorias03)
col3.subheader('Ejercicio')
col3.image("https://i.pinimg.com/736x/fc/ee/5e/fcee5e34cc920fdc291fb7307cd20c1b.jpg")
if (Edad > 17):
  col3.write("Los adultos de 18 a 64 años deberían acumular un mínimo de 150 minutos semanales de actividad física aeróbica moderada, o bien un mínimo de 75 minutos semanales de actividad aeróbica vigorosa, o bien una combinación equivalente de actividad moderada y vigorosa.")
else:
  col3.write("Los niños de 5 a 17 años necesitan acumular un mínimo de 60 minutos diarios de actividad física moderada o vigorosa.")
st.subheader("Sobrepeso y obesidad en población")
st.image("https://www.24-horas.mx/wp-content/uploads/2020/11/kilos.jpg")
st.subheader("Actvidad física en México")
st.image("https://cdn2.excelsior.com.mx/media/inside-the-note/pictures/2021/02/06/90.jpg")

df = pd.read_csv("https://raw.githubusercontent.com/juanpa129/Clase/main/Grafica%20streamlit.csv")
df
import plotly.express as px
fig = px.bar(df,x="Grado de inseguridad alimentarias",y=["2018","2020"])
st.subheader("Inseguridad alimentaria en México")
st.write(fig)

