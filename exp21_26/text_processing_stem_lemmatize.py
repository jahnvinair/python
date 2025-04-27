import re

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return text.split()

def simple_stem(word):
    # Basic Porter-like stemming rules
    if word.endswith('ies') and len(word) > 4:
        return word[:-3] + 'y'
    if word.endswith('s') and not word.endswith('ss'):
        return word[:-1]
    if word.endswith('ing') and len(word) > 5:
        return word[:-3]
    if word.endswith('ed') and len(word) > 4:
        return word[:-2]
    return word

def simple_lemmatize(word):
    # Simple lemmatization dictionary
    lemma_dict = {
        'ran': 'run',
        'running': 'run',
        'dogs': 'dog',
        'children': 'child',
        'better': 'good'
    }
    return lemma_dict.get(word, word)

def create_three_word_sequences(tokens):
    return [' '.join(tokens[i:i+3]) for i in range(len(tokens)-2)]

def main():
    file_path = input("Enter text file path (e.g., 'input.txt'): ")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("File not found.")
        return
    
    cleaned_text = clean_text(text)
    tokens = tokenize(cleaned_text)
    stemmed_tokens = [simple_stem(t) for t in tokens]
    lemmatized_tokens = [simple_lemmatize(t) for t in stemmed_tokens]
    
    print("Stemmed Tokens:")
    print(stemmed_tokens)
    print("Lemmatized Tokens:")
    print(lemmatized_tokens)
    print("3-Word Sequences (Lemmatized):")
    print(create_three_word_sequences(lemmatized_tokens))

if __name__ == "__main__":
    main()
