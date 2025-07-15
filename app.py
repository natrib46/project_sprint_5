import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

#Carregando os dados
df = pd.read_csv('vehicles.csv')

#Criando o cabeçalho
st.header("Dashboard - Análise de veículos")

#Descrição do projeto
st.write("""
Este projeto apresenta uma análise dos veículos com base nos dados disponíveis, incluindo a distribuição dos preços e a relação entre preço e quilometragem.
Use os checkboxes abaixo para visualizar os gráficos desejados.
""")

#Adicionando um subtitulo
st.subheader("Selecione o(s) gráfico(s) que deseja visualizar")







#Gráficos

#Botão para mostrar histograma dos preços
if st.button('Mostrar distribuição dos preços'):
    fig = px.histogram(df[df['price'] < 70000], x='price', nbins=50, title='Distribuição dos preços dos carros (até 70k)')
    fig.update_layout(xaxis_title='Preço (R$)', yaxis_title='Quantidade')
    st.plotly_chart(fig)


#Checkbox Preço x Quilometragem 
show_scatter = st.checkbox("Gráfico de dispersão Preço x Quilometragem")
if show_scatter:
    fig = px.scatter(df, x='odometer', y='price', title='Preço vs Quilometragem', opacity=0.5)
    fig.update_layout(xaxis_title='Quilometragem', yaxis_title='Preço (R$)')
    st.plotly_chart(fig)


#Checkbox Preço x Idade
current_year = datetime.now().year
df['vehicle_age'] = current_year - df['year']

show_price_age = st.checkbox("Gráfico Preço Médio por Idade do Carro")
if show_price_age:
    price_by_age = df.groupby('vehicle_age')['price'].mean().reset_index()
    fig_price_age = px.line(
        price_by_age,
        x='vehicle_age',
        y='price',
        title='Preço Médio por Idade do Carro',
        labels={'vehicle_age': 'Idade do carro (anos)', 'price': 'Preço Médio (R$)'},
    )
    st.plotly_chart(fig_price_age)



#Checkbox Preço x Marca
show_price_brand = st.checkbox("Preço médio por marca de carro")
if show_price_brand:
    price_by_brand = df.groupby('brand')['price'].mean().reset_index().sort_values(by='price', ascending=False)
    fig_price_brand = px.bar(
        price_by_brand,
        x='brand',
        y='price',
        title='Preço médio por marca de carro',
        labels={'brand': 'Marca', 'price': 'Preço médio (R$)'},
        color_discrete_sequence=['steelblue']
    )
    fig_price_brand.update_layout(xaxis_tickangle=-45)
    st.plotly_chart(fig_price_brand)