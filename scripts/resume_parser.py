# scripts/resume_parser.py

import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using pdfplumber.
    Returns the extracted text as a string.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def save_text_to_file(text, output_path):
    """
    Saves the extracted text to a .txt file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == "__main__":
    # Provide the relative path to your resume
    resume_path = "data/resumes/kunal_jain_resume.pdf"
    output_text_path = "data/processed/kunal_jain_resume_text.txt"

    if not os.path.exists(resume_path):
        print("Resume PDF not found. Please check the path.")
    else:
        extracted_text = extract_text_from_pdf(resume_path)
        save_text_to_file(extracted_text, output_text_path)
        print(f"Resume text extracted and saved to {output_text_path}")
