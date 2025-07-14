# scripts/skill_extractor.py

def load_skills(skill_file):
    """
    Loads a list of skills from a text file.
    Each line in the file should contain one skill.
    Returns a set of lowercased skills for easy matching.
    """
    with open(skill_file, 'r', encoding='utf-8') as f:
        skills = {line.strip().lower() for line in f if line.strip()}
    return skills

def load_resume_text(resume_file):
    """
    Loads cleaned resume text for skill extraction.
    """
    with open(resume_file, 'r', encoding='utf-8') as f:
        return f.read().lower()

def extract_skills_from_resume(resume_text, skill_set):
    """
    Extracts skills present in the resume by checking for keyword matches.
    Returns a sorted list of matched skills.
    """
    found_skills = set()
    for skill in skill_set:
        if skill in resume_text:
            found_skills.add(skill.title())  # Title case for readability
    return sorted(found_skills)

if __name__ == "__main__":
    skill_file = "data/skills_list.txt"
    resume_file = "data/processed/kunal_jain_resume_cleaned.txt"
    output_file = "data/processed/kunal_jain_extracted_skills.txt"

    skill_set = load_skills(skill_file)
    resume_text = load_resume_text(resume_file)
    extracted_skills = extract_skills_from_resume(resume_text, skill_set)

    if extracted_skills:
        print("Skills Found in Resume:")
        for skill in extracted_skills:
            print("-", skill)
    else:
        print("No skills found in resume.")

    # Save extracted skills
    with open(output_file, 'w', encoding='utf-8') as f:
        for skill in extracted_skills:
            f.write(skill + '\n')

    print(f"\nExtracted skills saved to {output_file}")
