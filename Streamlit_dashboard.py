# Streamlit dashboard

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import statsmodels.tsa

tab1, tab2 = st.tabs(["EDA", "Modelling"])

def parser(s):
    return datetime.strptime(s, '%Y-%m-%d')

df_ptl = pd.read_csv('alllines_ptl_complete.csv', parse_dates=[0], index_col=0, date_parser=parser)

# Splitting the data for different lines
l1=df_ptl[df_ptl['line']==1]
l2=df_ptl[df_ptl['line']==2]
l15=df_ptl[df_ptl['line']==15]
l3=df_ptl[df_ptl['line']==3]
l4=df_ptl[df_ptl['line']==4]
l5=df_ptl[df_ptl['line']==5]

df_ptl.set_index('year_month', inplace=True)

df_ptl.index = pd.to_datetime(df_ptl.index)

# First tab of Streamlit dashboard
with tab1:
    st.title("São Paulo Subway System")
    st.header("A tool for analyzing subway demand in São Paulo")

    ## First visual

    ### Plotting all the lines
    fig1, ax1 = plt.subplots()

    L1 = plt.plot(l1['MDU (Business Days Mean)'],color='tab:brown')
    L2 = plt.plot(l2['MDU (Business Days Mean)'], color='tab:cyan')
    L3 = plt.plot(l3['MDU (Business Days Mean)'], color='tab:pink')
    L4 = plt.plot(l4['MDU (Business Days Mean)'], color='tab:red')
    L5 = plt.plot(l5['MDU (Business Days Mean)'], color='tab:orange')
    L15 = plt.plot(l15['MDU (Business Days Mean)'], color='tab:olive')

    plt.title("Demand Business Days Mean (MDU) along the years")
    ax1.legend(['L1', 'L2','L3','L4','L5','L15'], fontsize=12, loc='upper right', ncols = 3)
    ax1.set_ylabel('MDU')
    ax1.set_xlabel('Years')

    st.pyplot(fig=fig1)

    st.write("The demand is different pre and pos COVID. In 2020, the most critical year of the pandemic, there is a blunt decrease of the demand because of quarantine. In 2021, the demand starts increasing probably because of vaccination that started in January. It's visible that the demand has upward trend but the demand is still lower than before COVID probably because there is a higher number of Hybrid and Home Office jobs in São Paulo than there was before COVID.")

    ## Second visual: saturday demand

    ### Plotting all the lines
    fig2, ax2 = plt.subplots()

    L1 = plt.plot(l1['MSD (Saturdays Mean)'],color='tab:brown')
    L2 = plt.plot(l2['MSD (Saturdays Mean)'], color='tab:cyan')
    L3 = plt.plot(l3['MSD (Saturdays Mean)'], color='tab:pink')
    L4 = plt.plot(l4['MSD (Saturdays Mean)'], color='tab:red')
    L5 = plt.plot(l5['MSD (Saturdays Mean)'], color='tab:orange')
    L15 = plt.plot(l15['MSD (Saturdays Mean)'], color='tab:olive')

    plt.title("Saturday Mean Demand along the years")
    ax2.legend(['L1', 'L2','L3','L4','L5','L15'], fontsize=12, loc='upper right', ncols = 3)
    ax2.set_ylabel('Saturday Mean Demand')
    ax2.set_xlabel('Years')

    st.pyplot(fig=fig2)

    ## Second visual: sunday demand

    ### Plotting all the lines
    fig2, ax2 = plt.subplots()

    L1 = plt.plot(l1['MDO (Sundays Mean)'],color='tab:brown')
    L2 = plt.plot(l2['MDO (Sundays Mean)'], color='tab:cyan')
    L3 = plt.plot(l3['MDO (Sundays Mean)'], color='tab:pink')
    L4 = plt.plot(l4['MDO (Sundays Mean)'], color='tab:red')
    L5 = plt.plot(l5['MDO (Sundays Mean)'], color='tab:orange')
    L15 = plt.plot(l15['MDO (Sundays Mean)'], color='tab:olive')

    plt.title("Sunday Mean Demand along the years")
    ax2.legend(['L1', 'L2','L3','L4','L5','L15'], fontsize=12, loc='upper right', ncols = 3)
    ax2.set_ylabel('Sunday Mean Demand')
    ax2.set_xlabel('Years')

    st.pyplot(fig=fig2)


    st.write("As subway is mostly used for people to travel to work, the demand is higher on working days.")

# Second tab of Streamlit dashboard
with tab2:
    st.title("São Paulo Subway System")
    st.header("A tool for modelling subway demand in São Paulo")

# Plot
df_ptl['total'].plot()

# Dickey-Fuller test
