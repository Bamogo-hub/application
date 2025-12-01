# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 16:38:06 2025

@author: BCS
"""
import numpy as np

def calc_whipple(series, ages):
    mask = (ages >= 23) & (ages <= 62)
    sub = series[mask]
    pop_05 = sub[ages[mask] % 5 == 0].sum()
    return (pop_05 * 5 / sub.sum()) * 100


def calc_myers(series, ages):
    counts = [series[ages % 10 == i].sum() for i in range(10)]
    total = series.sum()
    proportions = [(c / total * 100) for c in counts]
    deviations = sum(abs(p - 10) for p in proportions)
    return deviations / 2


def calc_bachi(series, ages):
    total = series.sum()
    exp = total / 10
    b = [abs(series[ages % 10 == i].sum() - exp) for i in range(10)]
    return 100 * sum(b) / total


def calc_un(series, ages):
    total = series.sum()
    exp = total / 5
    obs = [series[ages % 5 == i].sum() for i in range(5)]
    return (sum(abs(o - exp) for o in obs) / total) * 100


def compute_all_indices(df):
    ages = df["age"]

    return {
        "Whipple": {
            "Hommes": calc_whipple(df["hommes"], ages),
            "Femmes": calc_whipple(df["femmes"], ages),
            "Total": calc_whipple(df["total"], ages)
        },
        "Myers": {
            "Hommes": calc_myers(df["hommes"], ages),
            "Femmes": calc_myers(df["femmes"], ages),
            "Total": calc_myers(df["total"], ages)
        },
        "Bachi": {
            "Hommes": calc_bachi(df["hommes"], ages),
            "Femmes": calc_bachi(df["femmes"], ages),
            "Total": calc_bachi(df["total"], ages)
        },
        "ONU": {
            "Hommes": calc_un(df["hommes"], ages),
            "Femmes": calc_un(df["femmes"], ages),
            "Total": calc_un(df["total"], ages)
        }
    }
