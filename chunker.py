# chunker.py

def chunk_text(text, chunk_size=500, overlap=50):
    """
    text: pura document text
    chunk_size: ek chunk me kitne words
    overlap: previous chunk se kitne words repeat honge
    """

    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks
