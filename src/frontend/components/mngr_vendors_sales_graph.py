import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def mngr_vendors_sales_graph(data_vendedores, title, meta):
    df = pd.DataFrame(data_vendedores)

    #figura
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=df['Categorias'],
        y=df['Valores'],
        marker_color=['#344BFD', '#56B4E9', '#8280FF', '#D080FF','#000000'],
        name='vendas',
        width=0.3
    ))

    fig.add_shape(
        type='line',
        x0=-0.5,
        x1=len(df["Categorias"])-0.5,
        y0=meta,
        y1=meta,
        line=dict(color='#8280ff', width=4, dash='dash'),
        name='meta'
    )

    fig.add_annotation(
        x=len(df['Categorias']) - 0.5,
        y=meta,
        text=f"Meta: {meta}",
        showarrow=False,
        font=dict(size=12, color='white'),
        bgcolor='#1b2431',
        bordercolor='#8280ff',
    )

    fig.update_layout(
        title=title,
        xaxis_title="Vendedores",
        yaxis_title="Vendas (unidades)",
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgba(0,0,0,0)',
        font = dict(
            family = "Arial",
            size = 14,
            color = 'white',
            weight = 'bold'),
        barcornerradius = 14,
    )

    st.plotly_chart(fig)