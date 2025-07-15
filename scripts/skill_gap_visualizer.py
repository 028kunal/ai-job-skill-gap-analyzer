# scripts/skill_gap_visualizer.py

import matplotlib.pyplot as plt
from wordcloud import WordCloud

def load_skill_lists(skill_gap_file):
    """
    Loads matched and missing skills from your skill gap analysis report.
    """
    with open(skill_gap_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    matched_skills = []
    missing_skills = []
    current_section = None

    for line in lines:
        line = line.strip()
        if line.lower().startswith("matched skills"):
            current_section = "matched"
        elif line.lower().startswith("missing skills"):
            current_section = "missing"
        elif line.startswith("- "):
            skill = line[2:]
            if current_section == "matched":
                matched_skills.append(skill)
            elif current_section == "missing":
                missing_skills.append(skill)
    return matched_skills, missing_skills

def plot_skill_counts(matched_skills, missing_skills):
    """
    Plots a bar chart showing counts of matched vs missing skills.
    """
    categories = ['Matched Skills', 'Missing Skills']
    counts = [len(matched_skills), len(missing_skills)]

    plt.figure(figsize=(6, 4))
    plt.bar(categories, counts, color=['green', 'red'])
    plt.title('Skill Gap Analysis Summary')
    plt.ylabel('Count')
    plt.savefig('visualizations/skill_gap_bar_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Bar chart saved to visualizations/skill_gap_bar_chart.png")

def plot_skill_pie_chart(matched_skills, missing_skills):
    """
    Plots a pie chart showing the proportion of matched vs missing skills.
    """
    labels = ['Matched Skills', 'Missing Skills']
    sizes = [len(matched_skills), len(missing_skills)]
    colors = ['#4CAF50', '#F44336']

    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
    plt.title('Skill Gap Analysis - Matched vs Missing Skills')
    plt.savefig('visualizations/skill_gap_pie_chart.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Pie chart saved to visualizations/skill_gap_pie_chart.png")

def plot_missing_skills_wordcloud(missing_skills):
    """
    Generates and saves a word cloud for missing skills.
    """
    text = " ".join(missing_skills)
    wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='Set2').generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Missing Skills Word Cloud')
    plt.savefig('visualizations/missing_skills_wordcloud.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Word cloud saved to visualizations/missing_skills_wordcloud.png")

if __name__ == "__main__":
    skill_gap_file = "data/processed/skill_gap_analysis.txt"
    matched_skills, missing_skills = load_skill_lists(skill_gap_file)

    plot_skill_counts(matched_skills, missing_skills)
    plot_skill_pie_chart(matched_skills, missing_skills)
    plot_missing_skills_wordcloud(missing_skills)

