import streamlit as st 
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dataset/pizzas.csv")

model = LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

st.set_page_config(page_title="Pizza Price Predictor", page_icon="🍕", layout="centered")

st.title("🍕 Pizza Price Predictor")
st.write("Este sistema estima o preço de uma pizza com base no seu diâmetro")
st.divider()

diametro = st.number_input("📏 Tamanho do diâmetro da pizza (cm):", min_value=0.0, step=0.5)

if diametro > 0:
    predicted_price = model.predict([[diametro]])[0][0]
    st.success(f"💰 Preço estimado: **R$ {predicted_price:.2f}**")
else:
    st.info("Por favor, insira um valor de diâmetro maior que zero.")