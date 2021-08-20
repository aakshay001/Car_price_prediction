# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
# Define a function 'app()' which accepts 'car_df' as an input.
def app(car_df):
  st.title("Cars Data Visualisation")
  st.header("Visualise Data")
  st.subheader("Visualiser Selector")
  st.set_option('deprecation.showPyplotGlobalUse', False)

  features_list = st.multiselect("Select the x-axis values",('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick'))
  for feature in features_list:
    st.subheader(f"Scatterplot Between {feature} and Price")
    plt.figure(figsize=(10,8))
    sns.scatterplot(feature,"price",data = car_df,hue=feature)
    st.pyplot()

  st.subheader("Visualisation Selector")
  plot_type = st.multiselect("Select Charts/Plots",("Histogram","Box Plot","Correlation Heatmap"))
  if "Histogram" in plot_type:
    st.subheader("Histogram")
    column = st.selectbox("Select the column to create Histogram",('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(10,8))
    plt.hist(car_df[column],bins="sturges")
    st.pyplot()

  if "Box Plot" in plot_type:
    st.subheader("Box Plot")
    column = st.selectbox("Select the column to create Box Plot",('carwidth', 'enginesize', 'horsepower'))
    plt.figure(figsize=(10,8))
    sns.boxplot(car_df[column])
    st.pyplot()

  if "Correlation Heatmap" in plot_type:
    st.subheader("Correlation Heatmap")
    
    plt.figure(figsize=(10,8))
    sns.heatmap(car_df.corr(),annot = True)
    st.pyplot()  
