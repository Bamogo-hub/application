# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:39:09 2025

@author: BCS
"""
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px
def pyramide_age(df):
    # ---- Préparation des données ----
    # On crée une colonne "gender" pour pouvoir utiliser un style similaire au tien
    df_m = df[['age', 'hommes']].copy()
    df_m['gender'] = 'M'
    df_m.rename(columns={'hommes': 'count'}, inplace=True)

    df_f = df[['age', 'femmes']].copy()
    df_f['gender'] = 'F'
    df_f.rename(columns={'femmes': 'count'}, inplace=True)

    # Fusion des deux pour faciliter la manipulation
    data = pd.concat([df_m, df_f], ignore_index=True)

    # ---- Traces hommes et femmes ----
    trace_male = go.Bar(
        x=data[(data["gender"] == "M")]["count"] * -1,   # Hommes négatifs
        y=data[(data["gender"] == "M")]["age"],
        orientation="h",
        name="Hommes",
        marker=dict(color="#1f77b4")
    )

    trace_female = go.Bar(
        x=data[(data["gender"] == "F")]["count"],         # Femmes positifs
        y=data[(data["gender"] == "F")]["age"],
        orientation="h",
        name="Femmes",
        marker=dict(color="#d62728")
    )

    # ---- Layout ----
    layout = go.Layout(
        title="Pyramide des âges",
        xaxis=dict(title="Population"),
        yaxis=dict(title="Âge"),
        bargap=0.1,
        barmode="overlay"
    )

    # ---- Figure ----
    fig = go.Figure(data=[trace_male, trace_female], layout=layout)
    return fig






def indices_bar_chart(results):
    """
    results : dict avec les indices { 'Whipple': [val_Hommes, val_Femmes, val_Total], ... }
    """
    # Transformer en DataFrame
    df_results = pd.DataFrame(results, index=['Hommes','Femmes','Total'])
    
    # Transformer en format long pour Plotly
    df_plot = df_results.reset_index().melt(
        id_vars='index', var_name='Indice', value_name='Valeur'
    )
    df_plot.rename(columns={'index':'Population'}, inplace=True)
    
    # Créer la figure Plotly
    fig = px.bar(
        df_plot,
        x='Indice',
        y='Valeur',
        color='Population',
        barmode='group',
        text='Valeur',
        title='Indices démographiques'
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    
    return fig

