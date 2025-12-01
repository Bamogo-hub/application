# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:42:07 2025

@author: BCS
"""

import streamlit as st

st.title("Statistiques descriptives")

if "df" not in st.session_state:
    st.warning("Veuillez importer un fichier dans l'accueil.")
else:
    df = st.session_state["df"]
    st.subheader("Résumé")
    st.dataframe(df.describe())

    st.subheader("Population totale")
    st.write(f"Hommes : {df['hommes'].sum():,.0f}")
    st.write(f"Femmes : {df['femmes'].sum():,.0f}")
    st.write(f"Total : {df['total'].sum():,.0f}")
