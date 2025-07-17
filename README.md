# AI Job Skill Gap Analyzer

AI-powered Streamlit application for analyzing skill gaps between your resume and a job description (JD) using PDF uploads, visual insights, and personalized recommendations.

## Features

- Upload Resume and JD PDFs for analysis.
- Automatically extracts and cleans text from PDFs.
- Compares extracted skills from the resume and JD.
- Identifies matched skills and missing skills (skill gaps).
- Provides visual dashboards:
  - Pie chart for skill distribution.
  - Bar chart for comparison.
  - Word cloud for missing skills.
- Generates personalized recommendations for improving missing skills.
- Downloadable markdown report for your analysis.

## Tech Stack

- Python 3.9+
- Streamlit
- pdfplumber
- wordcloud
- plotly
- matplotlib


## How It Works

1. Upload your Resume PDF and JD PDF in the sidebar of the application.
2. Click "Analyze Skill Gap" to start analysis.
3. The application will:
   - Extract and clean text from both PDFs.
   - Load a predefined list of skills for comparison.
   - Extract relevant skills from both the resume and JD.
   - Identify matched skills and missing skills (gaps).
4. Displays:
   - A summary of matched and missing skills.
   - Visual dashboards with pie chart, bar chart, and word cloud.
   - Recommendations for improving missing skills.
5. Allows downloading a markdown report of your analysis for reference and planning.

## Setup Instructions

1. Clone the repository:

git clone https://github.com/yourusername/ai-job-skill-gap-analyzer.git
cd ai-job-skill-gap-analyzer

yaml
Copy
Edit

2. (Recommended) Create and activate a virtual environment:

On macOS/Linux:
python -m venv venv
source venv/bin/activate

graphql
Copy
Edit
On Windows:
python -m venv venv
venv\Scripts\activate

markdown
Copy
Edit

3. Install the required dependencies:

pip install -r requirements.txt

markdown
Copy
Edit

4. Run the application:

streamlit run app.py

css
Copy
Edit

5. Open your browser and navigate to:

http://localhost:8501

markdown
Copy
Edit

## Dependencies

All dependencies are listed in `requirements.txt`, including:

- streamlit
- pdfplumber
- wordcloud
- plotly
- matplotlib

You can install them using:

pip install -r requirements.txt

csharp
Copy
Edit

## Future Enhancements

- AI-based recommendations for courses to address skill gaps.
- ATS compatibility scoring for resume optimization.
- LinkedIn integration for live skill verification.
- User authentication for persistent dashboards.


## Contact

For any questions, suggestions, or collaboration opportunities, please reach out:

Email: kunalpjain02@gmail.com  
LinkedIn: https://www.linkedin.com/in/kunal-028-jain