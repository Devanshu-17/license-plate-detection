#create a streamlit app with the title "License Plate Detection App" and a description "Upload an image to detect the license plate"
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.colored_header import colored_header


colored_header(
    label="License Plate Detection App",
    description="",
    color_name="violet-70",
)

st.write("This app detects the license plate of a car in an image")
colored_header(
    label="How to use",
    description="",
    color_name="red-70",
)

st.markdown("1. Upload an image")
st.markdown("2. Click the **Detect License Plate** button")
st.markdown("3. The license plate number will be displayed")

#add a button to switch to the "🚔 License Plate Detection" page
if st.button("🚔 License Plate Detection"):
    switch_page("detection")

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://images.unsplash.com/photo-1567360425618-1594206637d2?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=868&q=80");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()


def add_logo():
    st.markdown(
        f"""
        <style>
            [data-testid="stSidebarNav"] {{
                background-image: "./car.png";
                background-repeat: no-repeat;
                padding-top: 80px;
                background-position: 20px 20px;
                background-size: 50%;
            }}
            [data-testid="stSidebarNav"]::before {{
                content: "Detectron";
                font-family: "Apple Chancery", Helvetica, Arial, sans-serif;
                padding-left: 40px;
                padding-top: 20px;
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 90px;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()

from streamlit_extras.app_logo import add_logo
add_logo("./car.png", height=120)
