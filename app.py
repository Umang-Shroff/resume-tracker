import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_gemini_response(input):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(input)
    return response.text

def input_pdf_text(file):
    reader=pdf.PdfFileReader(file)
    text=""
    for page in reader(len(reader.pages)):
        page=reader.pages[page]
        text+=str(page.extract_text())
        

input_prompt="""
Hey Act like a skilled of very experienced ATS(Application Tracking System) with a 
deep understanding of tech field, software engineering, data science, data analyst 
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide best assistance for 
improving the resumes. Assign the percentage Matching based on Jd and the missing key words with 
high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"Job Desc Match":"%", "Missing keywords":"[]", "Profile Summary":""}}
"""

st.title("Smart ATS")
st.text("Improve your resume ATS")
jd=st.text_area("Enter the job description")
file=st.file_uploader("Upload your resume", type="pdf",help="Please upload your resume in pdf format")

submit = st.button("Submit")


if submit:
    if file is not None:
        text=input_pdf_text(file)
        response=get_gemini_response(input_prompt)
        st.subheader(response)