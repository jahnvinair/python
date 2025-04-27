import re

def load_stop_words():
    # Minimal stop words list (offline-compatible)
    return {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'for', 'on', 'with'}

def load_spell_dict():
    # Simple spell correction dictionary
    return {
        'teh': 'the',
        'recieve': 'receive',
        'definately': 'definitely',
        'occured': 'occurred'
    }

def clean_text(text):
    # Convert to lowercase, remove punctuation, numbers, extra spaces
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)      # Remove numbers
    text = re.sub(r'\s+', ' ', text)     # Normalize spaces
    return text.strip()

def tokenize(text):
    return text.split()

def remove_stop_words(tokens, stop_words):
    return [t for t in tokens if t not in stop_words]

def correct_spelling(tokens, spell_dict):
    return [spell_dict.get(t, t) for t in tokens]

def main():
    file_path = input("Enter text file path (e.g., 'input.txt'): ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return
    
    stop_words = load_stop_words()
    spell_dict = load_spell_dict()
    
    # Process text
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    tokens_no_stop = remove_stop_words(tokens, stop_words)
    corrected_tokens = correct_spelling(tokens_no_stop, spell_dict)
    
    print("Cleaned Tokens (after stop word removal and spell correction):")
    print(corrected_tokens)

if __name__ == "__main__":
    main()