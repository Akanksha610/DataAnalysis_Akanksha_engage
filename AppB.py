import streamlit as st
import plotly_express as px
import pandas as pd

def app():
    st.title("Cars Numeric Data Visualization")
    st.sidebar.subheader("Visualization Settings")
    uploaded_file=st.sidebar.file_uploader(label="Upload your CSV file."
    ,type=['csv'])
    if uploaded_file is not None:
        print("hello")
        df=pd.read_csv(uploaded_file)
    
    global numeric_columns
    try:
        numeric_columns=list(df.select_dtypes(['float','int']).columns)
    except Exception as e:
        #print(e)
        st.write("Please upload file to the Application")

    chart_select = st.sidebar.selectbox(
        label="Select the chart type",
        options=['Scatterplots','Lineplots','Violinplot']
    )

    CompanyName_options=df['company'].unique().tolist()

    if chart_select == 'Scatterplots':
        st.sidebar.subheader("Scatterplot Settings")
        try:
            x_values = st.sidebar.selectbox('X axis',options=numeric_columns)
            y_values = st.sidebar.selectbox('Y axis',options=numeric_columns)
            plot = px.scatter(data_frame=df,x=x_values, y=y_values)
            #display the chart
            st.plotly_chart(plot)
        except Exception as e:
            print(e)
    
    if chart_select=='Lineplots':
        st.sidebar.subheader("Lineplot Settings")
        try:
            x_values=st.sidebar.selectbox('X axis',options=numeric_columns)
            y_values=st.sidebar.selectbox('Y axis',options=numeric_columns)
            #options=st.multiselect('Which country plot you want to see',CompanyName_options)
            plot=px.bar(df,x=x_values,y=y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select=='Violinplot':
        st.sidebar.subheader("Violinplot Settings")
        try:
            value=st.sidebar.selectbox('Parameter',options=numeric_columns)
            plot=px.violin(df,y=value)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)