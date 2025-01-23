import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf 
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))