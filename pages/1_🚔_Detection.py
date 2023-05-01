import cv2
import numpy as np
import pytesseract
import streamlit as st
from matplotlib import pyplot as plt
import imutils


def detect_license_plate(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    bfilter = cv2.bilateralFilter(gray, 11, 17, 17) #Noise reduction
    edged = cv2.Canny(bfilter, 30, 200) #Edge detection
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    mask = np.zeros(gray.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0,255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
    (x,y) = np.where(mask==255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = gray[x1:x2+1, y1:y2+1]
    st.image(cropped_image)
    text = pytesseract.image_to_string(cropped_image, lang='eng')
    if text:
        return text.strip()
    else:
        return None

def app():
    st.title("License Plate Detection App")
    st.write("Upload an image to detect the license plate")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg","jpeg","png"])
    if uploaded_file is not None:
        image = np.array(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        st.image(image, channels="BGR")
        if st.button("Detect License Plate"):
            license_plate = detect_license_plate(image)
            if license_plate:
                st.write("License plate number:", license_plate)
            else:
                st.write("License plate not detected")

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



if __name__ == "__main__":
    add_bg_from_url()
    app()
