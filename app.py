# app.py

import streamlit as st
import pdfplumber
import os
from scripts.text_cleaner import clean_text
from scripts.skill_extractor import load_skills, extract_skills_from_resume
from scripts.skill_gap_analysis import load_skills_from_file
import matplotlib.pyplot as plt
from wordcloud import WordCloud 

# ---------- Helper Functions ----------
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def plot_skill_summary(matched_skills, missing_skills):
    labels = ['Matched Skills', 'Missing Skills']
    sizes = [len(matched_skills), len(missing_skills)]
    colors = ['#4CAF50', '#F44336']

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    ax.set_title('Skill Gap Analysis - Matched vs Missing Skills')
    st.pyplot(fig)

def plot_skill_bar_chart(matched_skills, missing_skills):
    categories = ['Matched Skills', 'Missing Skills']
    counts = [len(matched_skills), len(missing_skills)]

    fig, ax = plt.subplots()
    ax.bar(categories, counts, color=['#4CAF50', '#F44336'])
    ax.set_title('Skill Gap Analysis - Count Comparison')
    ax.set_ylabel('Count')
    st.pyplot(fig)


def plot_missing_skills_wordcloud(missing_skills):
    if not missing_skills:
        st.info("No missing skills to display in word cloud.")
        return

    text = " ".join(missing_skills)
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    ax.set_title('Missing Skills Word Cloud')
    st.pyplot(fig)


# ---------- Streamlit App ----------
st.title("🧑‍💻 AI-Powered Job Skill Gap Analyzer")

st.markdown("Upload your **Resume** and **Job Description (JD)** PDFs below to analyze your skill gap automatically.")

resume_file = st.file_uploader("Upload your Resume PDF", type=["pdf"])
jd_file = st.file_uploader("Upload JD PDF", type=["pdf"])

if st.button("Analyze Skill Gap"):

    if resume_file and jd_file:
        st.success("Files uploaded successfully. Processing...")

        # Extract & clean resume
        resume_text = extract_text_from_pdf(resume_file)
        resume_cleaned = clean_text(resume_text)

        # Extract & clean JD
        jd_text = extract_text_from_pdf(jd_file)
        jd_cleaned = clean_text(jd_text)

        # Skill extraction
        skills_list_file = "data/skills_list.txt"
        skill_set = load_skills(skills_list_file)

        resume_skills = set(s.lower() for s in extract_skills_from_resume(resume_cleaned.lower(), skill_set))
        jd_skills = set(s.lower() for s in extract_skills_from_resume(jd_cleaned.lower(), skill_set))

        # Skill gap analysis
        matched_skills = sorted(resume_skills.intersection(jd_skills))
        missing_skills = sorted(jd_skills - resume_skills)

        st.subheader("✅ Matched Skills")
        if matched_skills:
            st.write(", ".join([s.title() for s in matched_skills]))
        else:
            st.write("No matched skills found.")

        st.subheader("⚠️ Missing Skills (Skill Gaps)")
        if missing_skills:
            st.write(", ".join([s.title() for s in missing_skills]))
        else:
            st.write("No missing skills found.")

        st.subheader("📊 Skill Gap Visualization")
        plot_skill_summary(matched_skills, missing_skills)
        st.subheader("📊 Bar Chart of Skill Gap")
        plot_skill_bar_chart(matched_skills, missing_skills)
        st.subheader("☁️ Word Cloud of Missing Skills")
        plot_missing_skills_wordcloud(missing_skills)


    else:
        st.error("Please upload both Resume and JD PDFs to proceed.")
