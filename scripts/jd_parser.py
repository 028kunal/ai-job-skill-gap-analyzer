# scripts/jd_parser.py

import pdfplumber

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF using pdfplumber.
    Returns the extracted text as a single string.
    """
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

if __name__ == "__main__":
    pdf_path = "data/job_descriptions/sample_jd.pdf"
    output_path = "data/processed/sample_jd_text.txt"

    extracted_text = extract_text_from_pdf(pdf_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print(f"✅ JD text extracted and saved to {output_path}")
