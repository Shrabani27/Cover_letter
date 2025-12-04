import streamlit as st
from google.generativeai as genai

# Configure API
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Cover Letter Generator")

# User Inputs
job_title = st.text_input("Enter Job Title")
resume = st.text_area("Paste your resume summary here")

# Generate cover letter
if st.button("Generate cover letter"):
    prompt = f"""
    Write a professional cover letter for the job title "{job_title}".
    Use this resume summary:
    {resume}
    """

    # Generate output from Gemini
    response = model.generate_content(prompt)

    # Display result in Streamlit
    st.subheader("Generated Cover Letter")
    st.write(response.text)
