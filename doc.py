import streamlit as st
import openai
from PIL import Image
import requests
from io import BytesIO
import base64

# Configure OpenAI API
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to process image and detect disease
def process_image(image):
    # Convert image to base64 format
    img_data = image.read()
    image_bytes = BytesIO(img_data)
    image_pil = Image.open(image_bytes)

    # Convert image to base64 string
    img_base64 = base64.b64encode(img_data).decode()

    # Generate prompt for OpenAI based on the detected disease
    prompt = f"Analyze the image of {image_pil.filename} and detect the disease."

    # Call OpenAI API to analyze image and detect disease
    response = openai.ImageAnalyze.create(
        model="davinci",
        prompt=prompt,
        images=[img_base64],
        max_tokens=200
    )

    return response['text']

# Function to generate blog post
def generate_blog(title, content):
    st.subheader("Generated Blog Post")
    st.title(title)
    st.write(content)

# Streamlit app interface
def main():
    st.title("AI Health Blog Generator")

    st.subheader("Step 1: Upload an Image for Disease Detection")
    uploaded_image = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Button to analyze image and generate blog post
        if st.button("Analyze Image and Generate Blog Post"):
            detected_disease = process_image(uploaded_image)
            generate_blog(f"{detected_disease}: Understanding Symptoms, Treatments, and Prevention", "")

# Execute the app
if __name__ == "__main__":
    main()
