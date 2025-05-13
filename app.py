import streamlit as st 
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("pizzas.csv")

model = linear_model.LinearRegression()

x = df[["diametro"]]
y = df[["preco"]]

st.title("Pizza Price Predictor")