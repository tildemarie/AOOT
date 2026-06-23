#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 14:29:24 2026

@author: pikachu
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.ndimage import maximum_filter


folder = "/home/pikachu/LSSS/LSSS-Data/S1_PHavfisken[1]/Reports/"

def read_lsss_type16(filename):
    """
    Read LSSS Type 16 report into DataFrame.
    """

    with open(filename, 'r') as f:
        lines = f.readlines()

    # find header row
    header_idx = None
    for i, line in enumerate(lines):
        if line.startswith("YEAR"):
            header_idx = i
            break

    if header_idx is None:
        raise ValueError(f"No header found in {filename}")

    header = lines[header_idx].split()

    data = []

    for line in lines[header_idx+1:]:

        parts = line.split()

        if len(parts) != len(header):
            continue

        data.append(parts)

    df = pd.DataFrame(data, columns=header)

    # convert numeric columns
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    return df

def heatPlot(df):
    """
    df = df.reset_index(drop=True)

    # Create ping number
    df['ping'] = np.arange(len(df)) // 20

    # Pivot table
    heat = df.pivot_table(
    index='CH',
    columns='ping',
    values='He/Sp',
    aggfunc='mean'
    )

    plt.figure(figsize=(15, 6))

    sns.heatmap(
        heat,
        cmap='viridis',
        cbar_kws={'label': 'He/Sp'}
    )

    plt.xlabel('Ping')
    plt.ylabel('Depth Cell (CH)')
    plt.title('He/Sp through time')
    
    # Make shallow water appear at top
    plt.gca().invert_yaxis()
    
    plt.tight_layout()
    plt.show()
    """
    heat = df.pivot_table(
        index='PDMEAN',
        columns='UTC',
        values='He/Sp',
        aggfunc='mean'
    )

    data = heat.fillna(0).values
    
    # create mask of signal presence
    mask = data > 0
    
    # spread signal to neighbours (3x3 kernel)
    expanded_mask = maximum_filter(mask.astype(int), size=(3, 3))
    
    # apply original values where signal exists
    heat_dilated = np.where(expanded_mask, data, 0)

    heat = heat.sort_index(ascending=False)  # depth increasing downward

    heat_masked = heat.replace(0, np.nan)
    
    heat_smooth = heat.interpolate(
        axis=1,        # interpolate along time axis
        method='linear',
        limit=5        # controls smoothing strength
    )

    plt.figure(figsize=(18, 6))
    
    ax = sns.heatmap(
        heat_masked,
        cmap='turbo',
        cbar_kws={'label': 'He/Sp'},
        xticklabels=200
    )
    
    ax.set_xlabel('Time (UTC)')
    ax.set_ylabel('Depth (m)')
    ax.set_title('Herring/Sprat NASC vs Depth and Time')
    
    ax.invert_yaxis()
    
    plt.tight_layout()
    plt.show()

"""
def heatPlot2(df):
    
    for i in arrange(result):
        
"""        

result = read_lsss_type16(folder + "ListUserFile16__F038000_T1_0610.txt")
heatPlot(result)
