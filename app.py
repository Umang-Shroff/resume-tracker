import streamlit as st
import google.generativeai as genai
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import torch
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
 
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')  


def get_gemini_response(jd, text): 
    job_desc_embedding = semantic_model.encode(jd, convert_to_tensor=True)
    resume_embedding = semantic_model.encode(text, convert_to_tensor=True)
 
    similarity_score = cosine_similarity(job_desc_embedding.cpu().detach().numpy().reshape(1, -1),
                                         resume_embedding.cpu().detach().numpy().reshape(1, -1))

    similarity_percentage = float(similarity_score[0][0]) * 100  

    input_prompt = f"""
    You are a highly skilled and experienced ATS (Application Tracking System) evaluator with deep expertise in the tech field, including software engineering, data science, data analysis, and big data engineering. Your task is to thoroughly analyze the provided resume based on the given job description. Consider the highly competitive job market and provide an in-depth evaluation of the resume's suitability for the position.

    The evaluation should cover the following points:
    1. **Job Description Match**: Determine the percentage match between the resume and the job description based on key skills, qualifications, and experience. This should be an overall percentage score.
    2. **Missing Keywords/Skills**: Identify any essential keywords, skills, or qualifications that are mentioned in the job description but are missing or underrepresented in the resume. List them clearly.
    3. **Experience Relevance**: Assess the relevance of the candidate's experience to the job description. Highlight any mismatches or gaps.
    4. **Profile Summary**: Provide a summary of the candidate's profile based on the resume content. Include strengths, potential areas for improvement, and overall suitability for the role.
    5. **Suggestions for Improvement**: Offer specific suggestions on how the resume could be improved, such as adding missing skills, clarifying experience, or emphasizing key achievements.

    Here is the format you should follow for your response:
    {{
      "Job Desc Match": "{similarity_percentage}%",
      "Missing Keywords": ["keyword1", "keyword2", "keyword3"],
      "Experience Relevance": "high/medium/low",
      "Profile Summary": "short summary of the candidate",
      "Suggestions for Improvement": ["suggestion1", "suggestion2"]
    }}
    Resume: {text}
    Job Description: {jd}
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

st.title("ATS Scanner")
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
