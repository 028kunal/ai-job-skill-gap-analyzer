# scripts/skill_gap_analysis.py

def load_skills_from_file(file_path):
    """
    Loads skills from a text file, returns a set of lowercased skills.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        return {line.strip().lower() for line in f if line.strip()}

if __name__ == "__main__":
    resume_skills_file = "data/processed/kunal_jain_extracted_skills.txt"
    jd_skills_file = "data/processed/sample_jd_extracted_skills.txt"
    output_file = "data/processed/skill_gap_analysis.txt"

    # Load skills
    resume_skills = load_skills_from_file(resume_skills_file)
    jd_skills = load_skills_from_file(jd_skills_file)

    # Compute matched and missing skills
    matched_skills = sorted(resume_skills.intersection(jd_skills))
    missing_skills = sorted(jd_skills - resume_skills)

    # Display results
    print("✅ Skill Gap Analysis Results:\n")

    print("Matched Skills:")
    if matched_skills:
        for skill in matched_skills:
            print("-", skill.title())
    else:
        print("None")

    print("\nMissing Skills (Skill Gaps):")
    if missing_skills:
        for skill in missing_skills:
            print("-", skill.title())
    else:
        print("None")

    # Save results to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("Matched Skills:\n")
        if matched_skills:
            for skill in matched_skills:
                f.write(f"- {skill.title()}\n")
        else:
            f.write("None\n")

        f.write("\nMissing Skills (Skill Gaps):\n")
        if missing_skills:
            for skill in missing_skills:
                f.write(f"- {skill.title()}\n")
        else:
            f.write("None\n")

    print(f"\n✅ Skill gap analysis saved to {output_file}")
