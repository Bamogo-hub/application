# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:41:26 2025

@author: BCS
"""
import streamlit as st
from utils.charts import pyramide_age

st.title("Pyramide des âges")

if "df" not in st.session_state:
    st.warning("Veuillez importer les données dans la page d’accueil.")
else:
    df = st.session_state["df"]
    fig = pyramide_age(df)
    st.plotly_chart(fig, use_container_width=True)
