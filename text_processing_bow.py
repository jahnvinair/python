import re
from sklearn.feature_extraction.text import CountVectorizer

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

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

def bag_of_words(docs):
    vectorizer = CountVectorizer()
    bow_matrix = vectorizer.fit_transform(docs)
    return vectorizer.get_feature_names_out(), bow_matrix.toarray()

def main():
    docs = read_documents()
    if not docs:
        return
    
    vocab, bow_matrix = bag_of_words(docs)
    print("Vocabulary:", vocab)
    print("Bag of Words Matrix:")
    for i in range(len(docs)):
        print(f"Document {i+1}: {bow_matrix[i]}")

if __name__ == "__main__":
    main()