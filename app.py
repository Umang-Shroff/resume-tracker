import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def get_gemini_response(jd, text):
    input_prompt = f"""
    Hey Act like a skilled and very experienced ATS(Application Tracking System) with a 
    deep understanding of the tech field, software engineering, data science, data analyst, 
    and big data engineering. Your task is to evaluate the resume based on the given job description.
    You must consider the job market is very competitive and you should provide the best assistance for 
    improving the resumes. Assign the percentage Matching based on JD and the missing keywords with 
    high accuracy.
    
    resume: {text}
    description: {jd}
    
    I want the response in one single string having the structure:
    {{"Job Desc Match":"%", "Missing keywords":"[]", "Profile Summary":""}}
    """
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(input_prompt)
        return response.text
    except Exception as e:
        return f"Error occurred: {e}"


def input_pdf_text(file):
    reader = PdfReader(file)  
    text = ""
    for page_num in range(len(reader.pages)): 
        page = reader.pages[page_num]
        text += page.extract_text()  
    return text

        

# input_prompt="""
# Hey Act like a skilled of very experienced ATS(Application Tracking System) with a 
# deep understanding of tech field, software engineering, data science, data analyst 
# and big data engineer. Your task is to evaluate the resume based on the given job description.
# You must consider the job market is very competitive and you should provide best assistance for 
# improving the resumes. Assign the percentage Matching based on Jd and the missing key words with 
# high accuracy
# resume:{text}
# description:{jd}

# I want the response in one single string having the structure
# {{"Job Desc Match":"%", "Missing keywords":"[]", "Profile Summary":""}}
# """

st.title("Smart ATS")
st.text("Improve your resume ATS")
jd=st.text_area("Enter the job description")
file=st.file_uploader("Upload your resume", type="pdf",help="Please upload your resume in pdf format")

submit = st.button("Submit")


if submit:
    if file is not None and jd.strip():
        text = input_pdf_text(file)
        response = get_gemini_response(jd, text)
        st.subheader(response)
    else:
        st.warning("Please provide both a job description and a resume.")
