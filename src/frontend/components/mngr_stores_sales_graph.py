import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def mngr_stores_sales_graph(data_lojas, title):

    df = pd.DataFrame(data_lojas)

    fig = go.Figure()

    cores = ['#E69F00', '#56B4E9', '#009E73', '#F0E442', '#0072B2','#D55E00','#CC79A7','#000000']
    line_styles = ['solid','dash','dot','dashdot']
    for i,loja in enumerate(df.columns[1:]):
        cor = cores[i % len(cores)]
        style = line_styles[i // len(cores) % len(line_styles)]
        fig.add_trace(go.Scatter(
            x=df['Mês'],
            y=df[loja],
            name=loja,
            line=dict(width=3,color=cor,dash=style)
        ))

    fig.update_layout(
        title = title,
        xaxis_title = "Mês",
        yaxis_title = "Valor Total de Vendas",
        legend_title = "Lojas",
        hovermode = "x unified",
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        font = dict(
            family = "Arial",
            size = 14,
            color = 'white',
            weight = 'bold')
    )

    st.plotly_chart(fig)    