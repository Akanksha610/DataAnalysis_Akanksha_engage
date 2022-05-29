import streamlit as st
import pickle
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn .compose import make_column_transformer
from sklearn.pipeline import make_pipeline
from streamlit_lottie import st_lottie
import json
import requests
import streamlit as st
from multipage_streamlit import State


def app():
    
    

    uploaded=st.sidebar.file_uploader(label="Upload your CSV file."
        , type=['csv'])
    
    if uploaded is not None:
           print("hello")
           df=pd.read_csv(uploaded)
           car=df
    
    global numeric_columns
    try:
        
        numeric_columns=list(df.select_dtypes(['float','int']).columns)
    except Exception as e:
          # print(e)
           st.write("Please upload file to the Application")

    
    #Cleaning of data and Training of data
    car = car. iloc [: , 1:]
    car[car['Price']>6e6]
    car=car[car['Price']<6e6].reset_index(drop=True)
    X=car.drop(columns='Price')
    y=car['Price']
    st.write(df)


    #Collection of unique data for options in select box
    Company=df.company.unique()
    
    shape=df.shape
    
    

    #Options For calculation of car price
    Brand=st.selectbox("Company",Company)

    df=df.loc[df['company']==Brand]
    Model=df.name.unique()
    year=df.year.unique()
    Fuel=df.fuel_type.unique()
   

    Model=st.selectbox("Model of car",Model)
    Year=st.selectbox("Year",year)
    Fuel=st.selectbox("Fueltype",Fuel)
    Km_travelled=st.slider("Travelled distance",0,100000,40)


    from sklearn.model_selection import train_test_split
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score
    from sklearn.preprocessing import OneHotEncoder
    from sklearn .compose import make_column_transformer
    from sklearn.pipeline import make_pipeline
    ohe=OneHotEncoder()
    ohe.fit(X[['name','company','fuel_type']])
    column_trans=make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),
                                    remainder='passthrough')
    lr=LinearRegression()
    pipe=make_pipeline(column_trans,lr)
    pipe.fit(X_train,y_train)
    y_pred=pipe.predict(X_test)

    scores=[]
    for i in range(1000):
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=i)
        lr=LinearRegression()
        pipe=make_pipeline(column_trans,lr)
        pipe.fit(X_train,y_train)
        y_pred=pipe.predict(X_test)
        scores.append(r2_score(y_test,y_pred))

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=np.argmax(scores))
    lr=LinearRegression()
    pipe=make_pipeline(column_trans,lr)
    pipe.fit(X_train,y_train)
    y_pred=pipe.predict(X_test)
    r2_score(y_test,y_pred)

    ok=st.button("Calculate Salary")
    if ok:
        ans=pipe.predict(pd.DataFrame([[Model,Brand,Year,Km_travelled,Fuel]]
        ,columns=['name','company','year','kms_driven','fuel_type']))
        st.write(ans[0])



