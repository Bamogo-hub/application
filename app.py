# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:35:42 2025

@author: BCS
"""
import streamlit as st
from utils.data import load_data

st.set_page_config(
    page_title="Indicateurs démographiques",
    layout="wide"
)

st.title("Bienvenue dans l’application d’analyse démographique")

st.markdown("""
Cette application vous permet de :
- Calculer les indices démographiques : **Whipple**, **Myers**, **Bachi**, **ONU**
- Visualiser la **pyramide des âges**
- Générer des **statistiques descriptives**
  
Commencez par importer un fichier CSV ou Excel contenant :
**age, hommes, femmes, total**.
""")

uploaded_file = st.file_uploader("Importer un fichier CSV ou Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.session_state["df"] = df
    st.success("Fichier chargé avec succès !")

    st.subheader("Aperçu des données")
    st.dataframe(df.head())
else:
    st.info("Veuillez importer un fichier pour activer les fonctionnalités dans les pages à gauche.")
