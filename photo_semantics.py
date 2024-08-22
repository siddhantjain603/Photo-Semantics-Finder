# Use a pipeline as a high-level helper
from transformers import pipeline
import streamlit as st
from PIL import Image

@st.cache_resource()
def load_model_pipeline(task):
    model = pipeline(task, model="Salesforce/blip-image-captioning-large")
    return model

st.markdown('<p class="title">Photo Semantics Finder</p>', unsafe_allow_html=True)

st.markdown(
    """
    <style>
        /* Style for title */
        .title {
            text-align: center !important;
            padding-bottom: 20px;
            color: white;
            font-size: 60px;
            font-weight: bold;
    </style>
    """,
    unsafe_allow_html=True
)

model = load_model_pipeline('image-to-text')

uploaded_image = st.file_uploader("Choose a photo", type=["jpg", "jpeg", "png"])

if st.button("Generate Semantics"):
    with st.spinner('Generating Semantics...'):
        col1, col2 = st.columns(2)
        with col1:
            st.image(uploaded_image, width=300)
        with col2:
            pil_image = Image.open(uploaded_image)
            semantics = model(images=pil_image)[0]['generated_text']
            st.subheader(semantics)