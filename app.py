import streamlit as st
import os
from apikey import openai_api_key, google_gemini_api_key
from openai import OpenAI
client = OpenAI(api_key=openai_api_key)
import google.generativeai as genai
from streamlit_carousel import carousel

genai.configure(api_key=google_gemini_api_key)

# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        "Generate a comprehensive engaging blog ost relevant to the given title and keywords  the blog should be make sure the Keywords are there in the blog post limited to the num_words words in length and suitable for online audience and ensure the content is original , informative and maintain a consistent tone throughout ",
      ],
    },
    {
      "role": "model",
      "parts": [
        "Please provide me with the following information so I can write an engaging and informative blog post for you:\n\n* **Blog Post Title:**  What is the exact title of your blog post?\n* **Keywords:** List all of the keywords you want to be included in the blog post.\n* **Number of Words (num_words):** How long should the blog post be? Please provide a specific word count. \n* **Target Audience:** Who are you trying to reach with this blog post? (e.g., beginners, experts, a specific age group, people interested in a particular hobby)\n\nOnce I have these details, I can create a high-quality blog post that meets your needs! \n",
      ],
    },
  ]
)

st.title("AI Writing Companion")

st.subheader("Welcome to the AI Writing Companion!")

with st.sidebar:
    st.title("Input details for the Blog Post")
    st.subheader("Details for Blog")

    blog_title = st.text_input("Blog Title", "")
    keywords = st.text_input("Keywords (comma-separated)")
    num_words = st.number_input("Number of Words", min_value=100, max_value=1000, step=250)
    num_images = st.number_input("Number of Images", min_value=1, max_value=5, step=1)
   
    submit_button = st.button("Generate Blog Post")

if submit_button:
    # Prepare the prompt for the AI model
    prompt = f"Write a blog post titled '{blog_title}' with the following keywords: {keywords}. The post should be approximately {num_words} words long."

    # Generate the blog post using the model
    images=[]

    # Extract the text from the response
    response = chat_session.send_message(prompt)
    for i in range(num_images):
        image_response = client.images.generate(
            model="dall-e-3",
            prompt="a white siamese cat",
            size="1024x1024",
            quality="standard",
            n=1,
        )
        images.append(image_response[0].url)

     
    for i in range(num_images):
        st.write(images[i])

    st.title("Your Blog Post")
    st.write(response.text)
