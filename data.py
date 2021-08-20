# S6.2: Design the View Data page of the multipage app.
# Import necessary modules
import numpy as np  
import pandas as pd
import streamlit as st

def app(car_df):
    # Displaying orginal dataset
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.beta_expander("View Dataset"):
        st.table(car_df)

    # Display descriptive statistics.
    st.subheader("Columns Description:")
    if st.checkbox("Show summary"):
        st.table(car_df.describe())    
    
    # ADD NEW CODE FROM HERE
    beta_col1,beta_col2 = st.beta_columns(2)

    with beta_col1:
      if st.checkbox("Show all column names"):
        st.table(list(car_df.columns))

    with beta_col2:
      if st.checkbox("View Column Data"):
        column_name = st.selectbox("Select column",tuple(car_df.columns))
        st.write(car_df[column_name])