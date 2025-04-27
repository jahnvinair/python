import re
from sklearn.preprocessing import Binarizer
import numpy as np

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def tokenize(text):
    return text.split()

def read_documents():
    docs = []
    for i in range(3):
        file_path = input(f"Enter path for text file {i+1} (e.g., 'doc{i+1}.txt'): ")
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
            docs.append(clean_text(text))
        except FileNotFoundError:
            print(f"File {file_path} not found.")
            return None
    return docs

def one_hot_encode(docs):
    # Tokenize and create vocabulary
    tokens = [tokenize(doc) for doc in docs]
    vocab = sorted(set(word for doc in tokens for word in doc))
    # Create frequency matrix
    freq_matrix = np.zeros((len(docs), len(vocab)), dtype=int)
    for i, doc_tokens in enumerate(tokens):
        for word in doc_tokens:
            if word in vocab:
                freq_matrix[i, vocab.index(word)] = 1
    # Binarize to ensure one-hot (0 or 1)
    binarizer = Binarizer()
    one_hot_matrix = binarizer.fit_transform(freq_matrix)
    return vocab, one_hot_matrix

def main():
    docs = read_documents()
    if not docs:
        return
    
    vocab, one_hot_matrix = one_hot_encode(docs)
    print("Vocabulary:", vocab)
    print("One-Hot Encoded Matrix:")
    for i in range(len(docs)):
        print(f"Document {i+1}: {one_hot_matrix[i]}")

if __name__ == "__main__":
    main()