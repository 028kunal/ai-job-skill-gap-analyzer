# scripts/spacy_tokenizer_test.py

import spacy

def load_cleaned_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

if __name__ == "__main__":
    # Load spaCy English model
    nlp = spacy.load("en_core_web_sm")

    # Load your cleaned resume
    resume_text = load_cleaned_resume("data/processed/kunal_jain_resume_cleaned.txt")

    # Pass text to spaCy pipeline
    doc = nlp(resume_text)

    # Sentence tokenization
    print("\n--- Sample Sentences ---")
    for i, sent in enumerate(doc.sents):
        print(f"{i+1}: {sent.text.strip()}")
        if i >= 4:  # show only first 5 for brevity
            break

    # Word tokenization
    print("\n--- Sample Tokens ---")
    for i, token in enumerate(doc):
        print(f"{i+1}: {token.text} | Lemma: {token.lemma_} | POS: {token.pos_}")
        if i >= 9:  # show only first 10 tokens for brevity
            break
