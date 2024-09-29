import streamlit as st
import os
from PIL import Image
import  google.generativeai as ga

ga.configure(api_key="AIzaSyCtzt682hLihZoAlgsY1814KXFZw7-J32k")

model = ga.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(input_test , image_date, prompt):
    response=model.generate_content([input_test,image_date[0],prompt])
    return response.text

def input_image_details(uploaded_file):
    if  uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts=[
            {
                 "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")

st.set_page_config(page_title="Invoice Checker")
st.sidebar.header("Ai Genda")
st.sidebar.write("Made by me ")
st.header("Invoice")
st.subheader("Powered by Ai Gemini")
input = st.text_input("What do u want to do", key="input")
uploaded_file = st.file_uploader("Choose and imgage ", type=["jpg", "png", "gif", "jpeg"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Uploaded Image", use_column_width=True)

ssubmit = st.button("Submit")

input_prompt = """
You are an expert in understanding calculus. I will upload a image of a problem and solve it step by step
"""

if ssubmit:
    image_date = input_image_details(uploaded_file)
    response = get_gemini_response(input, image_date, input)
    st.subheader("Here's what u need to know")
    st.write(response)
