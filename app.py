import streamlit as st
import pdfplumber
from scripts.text_cleaner import clean_text
from scripts.skill_extractor import load_skills, extract_skills_from_resume
from wordcloud import WordCloud
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import time

# ------------------ Page Setup ------------------
st.set_page_config(
    page_title="AI Job Skill Gap Analyzer",
    layout="wide"
)

# ------------------ Header ------------------
st.title("AI Job Skill Gap Analyzer")
st.write("Upload your Resume & Job Description PDFs — Analyze skills & gaps with AI insights")

# ------------------ Sidebar ------------------
st.sidebar.header("Skill Gap Analyzer")
st.sidebar.write("Analyze your resume vs JD with precision")
resume_file = st.sidebar.file_uploader("Upload Resume PDF", type=["pdf"])
jd_file = st.sidebar.file_uploader("Upload Job Description PDF", type=["pdf"])
analyze = st.sidebar.button("Analyze Skill Gap")

# ------------------ Helpers ------------------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text() + "\n"
    return text

def plot_pie_chart(matched, missing):
    fig = go.Figure(go.Pie(
        labels=["Matched Skills", "Missing Skills"],
        values=[len(matched), len(missing)],
        hole=0.5,
        marker=dict(colors=["#00fff0", "#ff6b6b"]),
    ))
    st.plotly_chart(fig, use_container_width=True)

def plot_bar_chart(matched, missing):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name='Skills Analysis',
        x=["Matched Skills", "Missing Skills"],
        y=[len(matched), len(missing)],
        marker_color=["#00fff0", "#ff6b6b"],
    ))
    st.plotly_chart(fig, use_container_width=True)

def plot_missing_skills_wordcloud(missing):
    if not missing:
        return
    wc = WordCloud(width=800, height=300, background_color="white").generate(" ".join(missing))
    fig, ax = plt.subplots(figsize=(8, 3))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig, use_container_width=True)

# ------------------ Main Logic ------------------
if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

if analyze:
    if not resume_file or not jd_file:
        st.error("Please upload both Resume and Job Description PDFs.")
    else:
        progress_bar = st.progress(0)
        status_text = st.empty()
        with st.spinner("Analyzing your documents..."):
            status_text.text("Extracting text from Resume...")
            progress_bar.progress(25)
            resume_text = extract_text_from_pdf(resume_file)
            status_text.text("Extracting text from Job Description...")
            progress_bar.progress(50)
            jd_text = extract_text_from_pdf(jd_file)
            status_text.text("Cleaning and processing text...")
            progress_bar.progress(75)
            resume_clean = clean_text(resume_text)
            jd_clean = clean_text(jd_text)
            status_text.text("Extracting and analyzing skills...")
            progress_bar.progress(90)
            skills_list_path = "data/skills_list.txt"
            skill_set = load_skills(skills_list_path)
            resume_skills = set(extract_skills_from_resume(resume_clean.lower(), skill_set))
            jd_skills = set(extract_skills_from_resume(jd_clean.lower(), skill_set))
            matched = sorted(resume_skills & jd_skills)
            missing = sorted(jd_skills - resume_skills)
            progress_bar.progress(100)
            status_text.text("Analysis complete!")
            time.sleep(0.5)
            progress_bar.empty()
            status_text.empty()

            # Store in session state
            st.session_state.matched = matched
            st.session_state.missing = missing
            st.session_state.jd_skills = jd_skills
            st.session_state.analysis_done = True

# ------------------ Display Analysis ------------------
if st.session_state.analysis_done:
    matched = st.session_state.matched
    missing = st.session_state.missing
    jd_skills = st.session_state.jd_skills

    st.header("Skills Analysis Results")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Matched Skills")
        if matched:
            st.write(", ".join(matched))
        else:
            st.info("No matched skills found.")

    with col2:
        st.subheader("Missing Skills (Skill Gaps)")
        if missing:
            st.write(", ".join(missing))
        else:
            st.success("No missing skills! You're well matched.")

    total_jd_skills = len(jd_skills)
    match_percentage = (len(matched) / total_jd_skills * 100) if total_jd_skills > 0 else 0

    st.write(f"Matched Skills: {len(matched)}")
    st.write(f"Missing Skills: {len(missing)}")
    st.write(f"Match Rate: {match_percentage:.1f}%")

    st.subheader("Visual Analysis Dashboard")
    tab1, tab2, tab3 = st.tabs(["Distribution", "Comparison", "Word Cloud"])
    with tab1:
        plot_pie_chart(matched, missing)
    with tab2:
        plot_bar_chart(matched, missing)
    with tab3:
        plot_missing_skills_wordcloud(missing)

    if missing:
        st.subheader("Personalized Recommendations")
        st.write("- Focus on the missing skills identified above.")
        st.write("- Consider taking online courses or certifications in these areas.")
        st.write("- Practice these skills through personal projects or freelance work.")

    report_content = f"""
# Skill Gap Analysis Report

## Summary
- Total JD Skills: {len(jd_skills)}
- Matched Skills: {len(matched)} ({match_percentage:.1f}%)
- Missing Skills: {len(missing)} ({100-match_percentage:.1f}%)

## Matched Skills
{', '.join(matched) if matched else 'None'}

## Missing Skills (Skill Gaps)
{', '.join(missing) if missing else 'None'}

## Recommendations
{'Focus on developing the ' + str(len(missing)) + ' missing skills listed above.' if missing else 'Great job! Your skills align well with the job requirements.'}

---
Generated by AI Job Skill Gap Analyzer
"""

    st.download_button(
        label="Download Report",
        data=report_content,
        file_name="skill_gap_analysis_report.md",
        mime="text/markdown",
        help="Download your analysis as a markdown file"
    )
