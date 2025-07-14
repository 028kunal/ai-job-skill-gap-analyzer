# scripts/text_cleaner.py

def clean_text(text):
    """
    Cleans extracted resume text:
    - Removes extra blank lines
    - Joins broken lines
    - Strips unnecessary whitespace
    """

    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        # Remove leading/trailing whitespaces
        stripped_line = line.strip()
        if stripped_line != "":
            cleaned_lines.append(stripped_line)

    # Join lines intelligently:
    # If the previous line does not end with punctuation, merge with current
    merged_lines = []
    buffer = ""
    for line in cleaned_lines:
        if buffer == "":
            buffer = line
        else:
            if buffer[-1] not in ".!?":
                buffer += " " + line
            else:
                merged_lines.append(buffer)
                buffer = line
    if buffer:
        merged_lines.append(buffer)

    cleaned_text = "\n".join(merged_lines)
    return cleaned_text


if __name__ == "__main__":
    # Test the cleaner
    with open("data/processed/kunal_jain_resume_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned_text = clean_text(raw_text)

    with open("data/processed/kunal_jain_resume_cleaned.txt", "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print("Cleaned text saved to data/processed/kunal_jain_resume_cleaned.txt")
