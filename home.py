import streamlit as st
from streamlit_lottie import st_lottie
import requests


def app():
    def load_lottieurl(url:str):
        r=requests.get(url)
        if r.status_code != 200:
           return None
        return r.json()
    lottie_hello=load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qufi1zre.json")
    st_lottie(
        animation_data=lottie_hello,
        speed=1,
        reverse= False,
        loop=True,
        quality="low",

        height="5",
        width="2",
        key=None,
    )   