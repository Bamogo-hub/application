# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:37:26 2025

@author: BCS
"""

import pandas as pd

def load_data(file):
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    df.columns = df.columns.str.lower()
    return df

