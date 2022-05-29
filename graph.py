import plotly.express as px
import streamlit as st
import seaborn as sns
import pandas as pd




def app():
#Data Cleaning
  df=pd.read_csv("C:/Users/Asus/Downloads/Carsfinal.csv")
  CompanyName = df['name'].apply(lambda x : x.split(' ')[0])
  df.insert(1,"CompanyName",CompanyName)
  df.drop(['name'],axis=1,inplace=True)
  df.head()
  df = df.drop_duplicates()
  df=df.dropna()
  cars=df



  #CompanyName_options = df['CompanyName'].unique().tolist()
  #CompanyName = st.selectbox('Stats of Which Company would you like to see',CompanyName_options,0)
  #df = df[df['CompanyName']==CompanyName]


#For top brands data
 

  print("Top 3 Trusted Brands")

  uniqueval=cars.CompanyName.unique()
  ans=[]
  ans.append(uniqueval[0])
  ans.append(uniqueval[1])
  ans.append(uniqueval[2])
  
  CompanyName = st.selectbox('Stats of Which Company would you like to see',ans,0)
  cars=cars[(cars.CompanyName == CompanyName) ]
  fig1 = px.bar(cars, x="year", y="price", color="CompanyName"
      , title=  CompanyName)
  fig1.update_layout(width=800)
  st.write(fig1)

  


  #cars2=cars1
  #uniqueval=cars1.CompanyName.unique()
  #cars1=cars1[(cars1.CompanyName == uniqueval[1]) ]
  #fig1 = px.bar(cars1, x="year", y="price", color="CompanyName"
 #, title=uniqueval[1])
  #fig1.update_layout(width=800)
  #st.write(fig1)


  #cars3=cars2
  #uniqueval=cars2.CompanyName.unique()
  #cars2=cars2[(cars2.CompanyName == uniqueval[2]) ]
  #fig1 = px.bar(cars2, x="year", y="price", color="CompanyName"
 #, title=uniqueval[2])
  #fig1.update_layout(width=800)
  #st.write(fig1)