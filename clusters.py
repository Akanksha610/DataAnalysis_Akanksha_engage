import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from kmodes.kprototypes import KPrototypes
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import re
from scipy.stats import zscore
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.feature_selection import f_regression, SelectKBest
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
import streamlit as st
import plotly_express as px
from streamlit_lottie import st_lottie
import requests
import json





def app():
    cars = pd.read_csv("C:/Users/Asus/Downloads/Carsfinal.csv")
    CompanyName = cars['name'].apply(lambda x : x.split(' ')[0])
    cars.insert(1,"CompanyName",CompanyName)
    cars.drop(['name'],axis=1,inplace=True)
 

    duplicate = cars[cars.duplicated()]


    cars = cars.drop_duplicates()


    cars=cars.dropna()

    cars_new=cars
    cars.isnull().sum()

    cars_new.drop(cars_new.iloc[:, 5:7], inplace = True, axis = 1)


    del cars_new['CompanyName']
    del cars_new['owner']
    del cars_new['maxpower']

    cars_new.drop(cars_new.iloc[:, 8:10], inplace = True, axis = 1)




    del cars_new['torque']
    del cars_new['seats']



    all_feature_cols = [col for col in cars_new.columns if col != "price"]

    # Series of feature:data type
    fdt = cars_new[all_feature_cols].dtypes

    # Identify numeric features
    all_numeric_features = fdt.index[fdt != "object"]

    skb = SelectKBest(
    score_func = f_regression,
    k = 3,
    )

    X = cars_new[all_numeric_features]
    y = cars_new["price"]

    X_new = skb.fit_transform(X, y)

    best_features = list(skb.get_feature_names_out())
    print("Top 3 features:", best_features)
    del cars_new['fuel']
    del cars_new['km_driven']
    del cars_new['year']

    X3=cars_new.iloc[:,1:]


    wcss = []
    for k in range(1,11):
        kmeans =KMeans(n_clusters=k, init="k-means++")
        kmeans.fit(X3)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(12,6))
    plt.grid()
    plt.plot(range(1,11),wcss,linewidth=2,color="red",marker="8")
    plt.xlabel("K-Value")
    plt.ylabel("WCSS")
    plt.show()

    i=st.slider("Number of clusters",2,10,2)

    color=["blue","green","yellow","red","cyan","lime","slategrey","navy","cornsilk","gold"]




    kmeans = KMeans(n_clusters=i)

    label = kmeans.fit_predict(X3)

    print(label)

    print(kmeans.cluster_centers_)

    clusters=kmeans.fit_predict(X3)
    cars_new["label"]=clusters

    from mpl_toolkits.mplot3d import Axes3D

    fig=plt.figure(figsize=(15,8))
    ax=fig.add_subplot(111,projection='3d')
    for k in range(0,i):
     #   ax.scatter(cars_new.price[cars_new.label==k],cars_new.mileage[cars_new.label==k],cars_new.engine[cars_new.label==k],c=color[k])
         ax.scatter(cars_new.price[cars_new.label==k],cars_new.mileage[cars_new.label==k],cars_new.engine[cars_new.label==k],c=color[k])
    #ax.scatter(cars_new.price[cars_new.label==1],cars_new.mileage[cars_new.label==1],cars_new.engine[cars_new.label==1],c='red')


    ax.view_init(30,185)
  
    plt.xlabel("price")
    plt.ylabel("mileage")
    ax.set_zlabel("engine")

    st.pyplot(fig)

