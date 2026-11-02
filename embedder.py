from sklearn.feature_extraction.text import TfidfVectorizer

def create_embeddings(texts):
    vectorizer = TfidfVectorizer(stop_words="english")
    embeddings = vectorizer.fit_transform(texts)
    return embeddings, vectorizer
