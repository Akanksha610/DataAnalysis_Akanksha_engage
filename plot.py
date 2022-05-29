import plotly.express as px
import streamlit as st
import seaborn as sns
import pandas as pd
from multipage_streamlit import State

def app():
    df=pd.read_csv("C:/Users/Asus/Downloads/Carsfinal.csv")
    #Data Cleaning
    CompanyName = df['name'].apply(lambda x : x.split(' ')[0])
    df.insert(1,"CompanyName",CompanyName)
    df.drop(['name'],axis=1,inplace=True)
    df.head()
    df = df.drop_duplicates()
    df=df.dropna()
    cars=df
    
    
    CompanyName_options=df['CompanyName'].unique().tolist()
    CompanyName=st.selectbox('Which Company would you like to see',CompanyName_options)
    df=df[df['CompanyName']==CompanyName]

    fig=px.scatter(df,x="year",y="price",size="price",color="CompanyName",
           hover_name="CompanyName",log_x=True,size_max=55,range_x=[1994,2020],
           range_y=[30000,10000000],animation_frame="CompanyName",animation_group="year"
    )

    fig.update_layout(width=800)
    st.write(fig)