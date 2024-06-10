import streamlit as st
from PIL import Image
from rembg import remove
from io import BytesIO

st.title("convert")

image_upload = st.file_uploader("Choisir une image", type=['png', 'jpg', 'jpeg'])

def convert_image(image):
    buf = BytesIO()
    image.save(buf, format='PNG')
    byte_im = buf.getvalue()
    return byte_im

if image_upload:
    image = Image.open(image_upload)
    fixed = remove(image)
    downloadable_image = convert_image(fixed)
    st.download_button("Télécharger l'image", downloadable_image, 'image_convert.png', 'image/png')