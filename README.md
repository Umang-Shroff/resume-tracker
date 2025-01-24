# ATS-Resume

## Overview

The **ATS Resume** is an intelligent system designed to help candidates optimize their resumes based on the job description. This system uses modern Natural Language Processing (NLP) techniques, including **semantic matching** using transformer models like **BERT** and **GPT**, to provide feedback and suggestions for improving resumes, making them more compatible with Applicant Tracking Systems (ATS).

### Key Features:
- **Job Description Matching**: The system evaluates how well a resume matches the job description.
- **Semantic Analysis**: Instead of relying on exact keyword matches, it uses semantic search to understand the context of words and sentences in the resume and job description.
- **Suggestions for Improvement**: The system offers actionable suggestions on how to improve resumes, highlighting missing skills or irrelevant experience.
- **PDF Resume Parsing**: The system allows users to upload their resumes in PDF format, extracts the text, and processes it for ATS evaluation.
- **ATS Simulation**: Replicates an actual ATS system by analyzing the relevance of the resume's content with the job description.

---

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.7 or higher
- Pip (for package management)

### Python Libraries

- **Streamlit**: For creating the web interface.
- **Google Generative AI (Gemini)**: For generating responses based on the input data.
- **PyPDF2**: For reading and extracting text from PDF resumes.
- **Sentence-Transformers**: For semantic similarity between job descriptions and resumes.
- **Torch**: For running the deep learning models.
- **Sklearn**: For cosine similarity calculation.
- **Dotenv**: For managing environment variables securely.

To install the required libraries, run the following command:

```bash
pip install streamlit google-generativeai PyPDF2 sentence-transformers torch sklearn python-dotenv
