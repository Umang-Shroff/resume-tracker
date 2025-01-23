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