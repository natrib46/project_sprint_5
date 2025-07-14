import streamlit as st
import pandas as pd
import plotly.express as px

#Carregando os dados
df = pd.read_csv('vehicles.csv')

#Criando o cabeçalho
st.header("Dashboard - Análise de veículos")

#Botão para mostrar histograma
if st.button('Mostrar distribuição dos preços'):
    fig = px.histogram(df[df['price'] < 70000], x='price', nbins=50, title='Distribuição dos preços dos carros (até 70k)')
    fig.update_layout(xaxis_title='Preço (R$)', yaxis_title='Quantidade')
    st.plotly_chart(fig)


show_scatter = st.checkbox("Mostrar gráfico de dispersão")
if show_scatter:
    fig = px.scatter(df, x='odometer', y='price', title='Preço vs Quilometragem', opacity=0.5)
    fig.update_layout(xaxis_title='Quilometragem', yaxis_title='Preço (R$)')
    st.plotly_chart(fig)