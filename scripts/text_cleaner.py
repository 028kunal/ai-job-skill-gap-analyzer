# scripts/text_cleaner.py

def clean_text(text):
    """
    Cleans extracted text:
    - Removes extra blank lines
    - Joins broken lines intelligently
    - Strips unnecessary whitespace
    """
    lines = text.splitlines()
    cleaned_lines = []

    for line in lines:
        stripped_line = line.strip()
        if stripped_line != "":
            cleaned_lines.append(stripped_line)

    # Join lines intelligently:
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
    # ✅ CONFIG: Change these paths to clean the desired file (resume or JD)
    input_file = "data/processed/sample_jd_text.txt"
    output_file = "data/processed/sample_jd_cleaned.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned_text = clean_text(raw_text)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(cleaned_text)

    print(f"✅ Cleaned text saved to {output_file}")
