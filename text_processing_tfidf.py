import re
from sklearn.feature_extraction.text import TfidfVectorizer

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

def tfidf(docs):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    return vectorizer.get_feature_names_out(), tfidf_matrix.toarray()

def main():
    docs = read_documents()
    if not docs:
        return
    
    vocab, tfidf_matrix = tfidf(docs)
    print("Vocabulary:", vocab)
    print("TF-IDF Matrix:")
    for i in range(len(docs)):
        print(f"Document {i+1}: {np.round(tfidf_matrix[i], 2)}")

if __name__ == "__main__":
    main()