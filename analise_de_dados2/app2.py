import streamlit as st
import pandas as pd
import plotly.express as px

#CRIAÇÃO DO TÍTULO
st.title("Dashboard de Funcionários")

#CAREGAMENTO DOS DADOS
df = pd.read_csv("novos_dados.csv")
st.subheader("Tabela de dados")
st.dataframe(df)

#CRIAÇÃO DE FILTROS
depart = st.selectbox("Selecione o departamento",df["departamento"].unique())
df_filtrado = df[df["departamento"] == depart]
st.subheader("Dados Filtrados")
st.write(df_filtrado)

#ELABORAÇÃO DO GRÁFICO

barra = px.bar(
        df_filtrado,
        x="nome_completo",
        y= "salario_mensal_brl",
        color="departamento",
        title = "Funcionários"
)

st.plotly_chart(barra)