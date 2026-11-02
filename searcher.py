from sklearn.metrics.pairwise import cosine_similarity

def search(query, chunks, embeddings, vectorizer, top_k=1):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, embeddings)[0]

    best_idx = similarities.argmax()
    best_score = similarities[best_idx]

    return chunks[best_idx], float(best_score)
