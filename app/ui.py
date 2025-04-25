import streamlit as st
from PIL import Image
from preprocessing import preprocess_image
from ocr_engine import extract_text_from_image, extract_fields

st.title("📄 Personal Loan Document OCR Processor")

uploaded_file = st.file_uploader("Upload Document", type=["jpg", "jpeg", "png", "pdf"])

if uploaded_file:
    image = Image.open(uploaded_file)
    processed_img = preprocess_image(image)
    st.image(processed_img, caption="Preprocessed Image")

    ocr_text = extract_text_from_image(processed_img)
    st.subheader("📃 OCR Extracted Text")
    st.text_area("OCR Output", ocr_text, height=200)

    st.subheader("🔍 Extracted Fields")
    fields = extract_fields(ocr_text)
    for key, value in fields.items():
        fields[key] = st.text_input(f"{key}:", value)

    if st.button("Submit"):
        st.success("Data submitted successfully!")
