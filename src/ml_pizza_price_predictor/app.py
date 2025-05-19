import streamlit as st 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dataset/pizzas.csv")

model = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

st.title("Pizza Price Predictor")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da Pizza: ")

if diametro:
    predicted_price = model.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza com diâmetro de {diametro} é de R${predicted_price}")