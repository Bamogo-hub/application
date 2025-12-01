# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:40:28 2025

@author: BCS
"""
import streamlit as st
from utils.indices import compute_all_indices
from utils.charts import indices_bar_chart
import pandas as pd

st.title("Calcul des indices démographiques")

if "df" not in st.session_state:
    st.warning("Veuillez importer les données dans la page d’accueil.")
else:
    df = st.session_state["df"]
    results = compute_all_indices(df)

    st.subheader("Tableau des indices")
    table = pd.DataFrame(results)
    st.dataframe(table)

    st.subheader("Graphique des indices")
    fig = indices_bar_chart(results)
    st.plotly_chart(fig, use_container_width=True)
