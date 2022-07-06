
import diabetes_home,diabetes_predict,diabetes_plots
import streamlit as st
import numpy as np
import pandas as pd


st.set_page_config(page_title = 'Early Diabetes Prediction Web App',
                    page_icon = 'random',
                    layout = 'wide',
                    initial_sidebar_state = 'auto'
                    )
@st.cache()
def load_data():
    df = pd.read_csv('https://s3-whjr-curriculum-uploads.whjr.online/b510b80d-2fd6-4c08-bfdf-2a24f733551d.csv')
    df.head()
    df.rename(columns = {"BloodPressure": "Blood_Pressure",}, inplace = True)
    df.rename(columns = {"SkinThickness": "Skin_Thickness",}, inplace = True)
    df.rename(columns = {"DiabetesPedigreeFunction": "Pedigree_Function",}, inplace = True) 
    return df

diabetes_df = load_data()

pages_dict = {"Home": "diabetes_home", 
           "Predict Diabetes": 'diabetes_predict', 
           "Visualise Decision Tree": 'diabetes_plots'}

st.sidebar.header('Navigation')
user_choice=st.sidebar.radio('Go to',(pages_dict.keys()))

selected_page=pages_dict[user_choice]

if selected_page=='diabetes_home':
    diabetes_home.app(diabetes_df)
elif selected_page=='diabetes_predict':
    diabetes_predict.app(diabetes_df)
elif selected_page=='diabetes_plots':
    diabetes_plots.app(diabetes_df)