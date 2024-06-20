### Project Title: AI Writing Companion

#### Project Overview
The AI Writing Companion is a Streamlit application designed to assist users in generating high-quality blog posts based on specified titles, keywords, and content length. It integrates Google's Gemini API for text generation and OpenAI's DALL-E API for image generation to create comprehensive blog content.

#### Features
- **Input Details for Blog Post**: Users can input the blog title, keywords (comma-separated), desired word count, and number of images to be included in the blog post.
- **Text Generation**: Utilizes Google's Gemini API to generate text content for the blog post based on user-provided details.
- **Image Generation**: Uses OpenAI's DALL-E API to generate images relevant to the blog post content.
- **Interactive UI**: Provides a user-friendly interface using Streamlit, with sidebar inputs for blog details and a main display area for generated content.

#### Installation and Setup
To run the AI Writing Companion on your local machine, follow these steps:

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/your_username/your_repository.git
   cd your_repository
   ```


2. Obtain API keys:
   - **OpenAI API Key**: Obtain from OpenAI platform and update `openai_api_key` in `apikey.py`.
   - **Google Gemini API Key**: Obtain from Google's developer console and update `google_gemini_api_key` in `apikey.py`.

3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```

#### Usage
1. Upon running the application, the main interface displays input fields for the blog title, keywords, word count, and number of images.
2. Users input their desired details and click on the "Generate Blog Post" button.
3. The application sends a prompt to the Gemini API to generate text content based on the provided inputs.
4. Simultaneously, it uses the OpenAI DALL-E API to generate images related to the blog post content.
5. Generated images are displayed, and the generated blog post text is shown in the application interface.

#### Technologies Used
- **Python**: Programming language used for backend logic.
- **Streamlit**: Framework for building interactive web applications for machine learning and data science.
- **OpenAI API**: Used for text generation.
- **Google Gemini API**: Utilized for additional text and content generation capabilities.
- **DALL-E API**: Provided by OpenAI for image generation based on text prompts.

#### Future Enhancements
- **Enhanced Image Generation**: Implement more sophisticated image generation techniques to produce more diverse and relevant visuals.
- **Natural Language Processing**: Incorporate NLP techniques for better understanding and refinement of generated text content.
- **User Authentication**: Add user authentication and saving capabilities for personalized blog post generation and storage.
- **Doc App**: We can use Gemini AI studio to input an image of any disease and then it gives a prompt template copy it and make a Python template code for GenAI projects and create a detailed blog page explaining the disease and its cure after successfully identifying it 
             
