import appA
import AppB
import plot
import clusters
import json
import home
import graph
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import requests

st.set_page_config(
        page_title="Cars24x7",
        page_icon="chart_with_upwards_trend",
        
    )
PAGES ={
"Home":home,
"Price Prediction": appA,
"Numeric Data Visualization": AppB,
"Graph":plot,
"Customer Segmentation":clusters,
"Top Companies":graph
    }
#st.sidebar.title('Navigation')
#selection = st.sidebar.radio("Go to", list(PAGES.keys()))
#page = PAGES[selection]
#page.app()


selected=option_menu(
menu_title=None,
#options=["Dataset","Data streamlit Analysis","Clusters","Predictons"],
options=list(PAGES.keys()),
icons=["file-earmark-bar-graph-fill","bar-chart-fill","","graph-down-arrow","pie-chart-fill"],
menu_icon="cast",
default_index=0,
orientation="horizontal",


)
page =PAGES[selected]
page.app()


st.title("Car Price Prediction")
uploaded_file=st.sidebar.file_uploader(label="Upload your CSV file."
    ,type=['csv'])
    
if uploaded_file is not None:
       print("hello")
       df=pd.read_csv(uploaded_file)
       car=df
    
global numeric_columns
try:
        
        numeric_columns=list(df.select_dtypes(['float','int']).columns)
except Exception as e:
         print(e)
         st.write("Please upload file to the Application")

    
    #Cleaning of data and Training of data
car = car. iloc [: , 1:]
car[car['Price']>6e6]
car=car[car['Price']<6e6].reset_index(drop=True)
X=car.drop(columns='Price')
y=car['Price']
def file():
    st.write(car)