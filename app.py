import pandas as pd
import plotly.express as px
import streamlit as st

# carros = pd.read_csv('vehicles.csv')

# hist_button = st.button('Criar histograma')

# if hist_button:
#     st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

#     fig = px.histogram(carros, x='odometer')

#     st.plotly_chart(fig, use_container_width=True)

# scat_button = st.button('Criar gráfico de dispersão')

# if scat_button:
#     st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')

#     fig2 = px.scatter(carros, x='odometer', y='price')

#     st.plotly_chart(fig2, use_container_width=True)

#-------------------------------------------------------------------------------------------
carros = pd.read_csv('vehicles1.csv')

sel_graf = st.selectbox(
    'Selecione o gráfico:',
    ('Gráfico histogram da coluna odometro', 'Gráfico de dispersão odometro x preço', 'Gráfico histogram ano de fabricação dos carros',
    'Gráfico quantidade dos modelos de carros', 'Gráfico de dispersão dos modelos de carros x preço',
    'Gráfico de dispersão do ano de fabricação dos carros x preço')
)

def plot_graf(grafico):
    if grafico == 'Gráfico histogram da coluna odometro':
        fig = px.histogram(carros, x='odometer')
    elif grafico == 'Gráfico de dispersão odometro x preço':
        fig = px.scatter(carros, x='odometer', y='price')
    elif grafico 'Gráfico histogram ano de fabricação dos carros':
        fig = px.histogram(carros, x='model_year')
    elif grafico 'Gráfico quantidade dos modelos de carros':
        fig = px.bar(carros, x='model')
    elif grafico 'Gráfico de dispersão dos modelos de carros x preço':
        fig = px.scatter(carros, x='model', y='price')
    elif grafico 'Gráfico de dispersão do ano de fabricação dos carros x preço':
        fig = px.scatter(carros, x='model_year', y='price')
    else:
        st.warning('Nenhum gráfico selecionado.')
        return

    st.plotly_chart(fig, use_container_width=True)

plot_graf(sel_graf)


#--------------------------------------------------------------------------------------

# st.write('Gráfico histogram da coluna odometro')
# odom_hist = px.histogram(carros, x='odometer')
# st.plotly_chart(odom_hist, use_container_width=True)

# st.write('Gráfico de dispersão odometro x preço')
# odom_scatter = px.scatter(carros, x='odometer', y='price')
# st.plotly_chart(odom_scatter, use_container_width=True)

# st.write('Gráfico histogram ano de fabricação dos carros')
# ymodel_hist = px.histogram(carros, x='model_year')
# st.plotly_chart(ymodel_hist, use_container_width=True)

# st.write('Gráfico quantidade dos modelos de carros')
# model_hist = px.bar(carros, x='model')
# st.plotly_chart(model_hist, use_container_width=True)

# st.write('Gráfico de dispersão dos modelos de carros x preço')
# model_scatter = px.scatter(carros, x='model', y='price')
# st.plotly_chart(model_scatter, use_container_width=True)

# st.write('Gráfico de dispersão do ano de fabricação dos carros x preço')
# ymodel_scatter = px.scatter(carros, x='model_year', y='price')
# st.plotly_chart(ymodel_scatter, use_container_width=True)



