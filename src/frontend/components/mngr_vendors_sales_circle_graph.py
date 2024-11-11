import streamlit as st
import plotly.graph_objects as go
import pandas as pd

def mngr_vendors_sales_circle_graph(data_vendedores, title):
    df = pd.DataFrame(data_vendedores)

    # Create the figure
    fig = go.Figure()

    fig.add_trace(go.Pie(
        labels=df['Categorias'],
        values=df['Valores'],
        marker_colors=['#344BFD', '#56B4E9', '#8280FF', '#D080FF', '#000000'],
        hole=0.5,
    ))

    fig.update_layout(
        title=title,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(
            family="Arial",
            size=14,
            color='white',
            weight='bold'
        ),
        showlegend=False,
        annotations=[dict(
            text=f'{sum(df["Valores"])} vendas',
            x=0.5,
            y=0.5,
            font_size=15,
            showarrow=False,
            font_family='Arial',
            font_color='white'
        )]
    )

    st.plotly_chart(fig)
